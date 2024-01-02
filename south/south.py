import requests
import xml.etree.ElementTree as ET
import ding
def daily_task():
    url = 'https://south-plus.net/plugin.php'
    params = {
        'H_name': 'tasks',
        'action': 'ajax',
        'actions': 'job',
        'cid': 15,
        'nowtime': 1704195091299,
        'verify': '94a180c7'
    }
    headers = {
        'authority': 'south-plus.net',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'eb9e6_cknum=CAMDAgBfAQYFCTtqDAQCAQQOWAIABlQHDQUIAFBTAQVUWlAPWAICVVICAQQ%3D; eb9e6_ck_info=%2F%09; eb9e6_winduser=CAMBAwdSAj9WAFdUAFICXFVdCFFXDlBXAAICAwACAVFRCAQIWlUABDg%3D; eb9e6_ol_offset=171108; peacemaker=1; eb9e6_lastpos=other; eb9e6_lastvisit=10%091704195078%09%2Fplugin.php%3FH_name-tasks.html',
        'referer': 'https://south-plus.net/plugin.php?H_name-tasks.html',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers, params=params)
    xml_data = response.text

    # 解析 XML 数据
    root = ET.fromstring(xml_data)

    # 提取 CDATA 部分
    cdata_text = root.text

    # 从 CDATA 中提取所需文本
    extracted_text = cdata_text.split('\t')[1]

    return extracted_text
def complete_daily_task():
    url = 'https://south-plus.net/plugin.php'
    params = {
        'H_name': 'tasks',
        'action': 'ajax',
        'actions': 'job2',
        'cid': 15,
        'nowtime': 1704195875365,
        'verify': '94a180c7'
    }
    headers = {
        'authority': 'south-plus.net',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'eb9e6_cknum=CAMDAgBfAQYFCTtqDAQCAQQOWAIABlQHDQUIAFBTAQVUWlAPWAICVVICAQQ%3D; eb9e6_ck_info=%2F%09; eb9e6_winduser=CAMBAwdSAj9WAFdUAFICXFVdCFFXDlBXAAICAwACAVFRCAQIWlUABDg%3D; eb9e6_ol_offset=171108; peacemaker=1; eb9e6_lastpos=other; eb9e6_lastvisit=798%091704195866%09%2Fplugin.php%3FH_name-tasks-actions-newtasks.html.html',
        'referer': 'https://south-plus.net/plugin.php?H_name-tasks-actions-newtasks.html.html',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers, params=params)
    xml_data = response.text

    # 解析 XML 数据
    root = ET.fromstring(xml_data)

    # 提取 CDATA 部分
    cdata_text = root.text

    # 从 CDATA 中提取所需文本
    extracted_text = cdata_text.split('\t')[1]

    return extracted_text

def weekly_task():
    url = 'https://south-plus.net/plugin.php'
    params = {
        'H_name': 'tasks',
        'action': 'ajax',
        'actions': 'job',
        'cid': 14,
        'nowtime': 1704196047109,
        'verify': '94a180c7'
    }
    headers = {
        'authority': 'south-plus.net',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'eb9e6_cknum=CAMDAgBfAQYFCTtqDAQCAQQOWAIABlQHDQUIAFBTAQVUWlAPWAICVVICAQQ%3D; eb9e6_ck_info=%2F%09; eb9e6_winduser=CAMBAwdSAj9WAFdUAFICXFVdCFFXDlBXAAICAwACAVFRCAQIWlUABDg%3D; eb9e6_ol_offset=171108; peacemaker=1; eb9e6_lastpos=other; eb9e6_lastvisit=972%091704196040%09%2Fplugin.php%3FH_name-tasks.html.html',
        'referer': 'https://south-plus.net/plugin.php?H_name-tasks.html.html',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers, params=params)
    xml_data = response.text

    # 解析 XML 数据
    root = ET.fromstring(xml_data)

    # 提取 CDATA 部分
    cdata_text = root.text

    # 从 CDATA 中提取所需文本
    extracted_text = cdata_text.split('\t')[1]

    return extracted_text

def complete_weekly_task():
    url = 'https://south-plus.net/plugin.php'
    params = {
        'H_name': 'tasks',
        'action': 'ajax',
        'actions': 'job2',
        'cid': 14,
        'nowtime': 1704196182949,
        'verify': '94a180c7'
    }
    headers = {
        'authority': 'south-plus.net',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'eb9e6_cknum=CAMDAgBfAQYFCTtqDAQCAQQOWAIABlQHDQUIAFBTAQVUWlAPWAICVVICAQQ%3D; eb9e6_ck_info=%2F%09; eb9e6_winduser=CAMBAwdSAj9WAFdUAFICXFVdCFFXDlBXAAICAwACAVFRCAQIWlUABDg%3D; eb9e6_ol_offset=171108; peacemaker=1; eb9e6_lastpos=other; eb9e6_lastvisit=1111%091704196179%09%2Fplugin.php%3FH_name-tasks-actions-newtasks.html.html',
        'referer': 'https://south-plus.net/plugin.php?H_name-tasks-actions-newtasks.html.html',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers, params=params)
    xml_data = response.text

    # 解析 XML 数据
    root = ET.fromstring(xml_data)

    # 提取 CDATA 部分
    cdata_text = root.text

    # 从 CDATA 中提取所需文本
    extracted_text = cdata_text.split('\t')[1]

    return extracted_text

ding.send_md(title="测试", text="# south: \n ## •  周：" + weekly_task() + "\n## •  周：" + complete_weekly_task() + "\n## •  天：" + daily_task() + "\n## •  天：" + complete_daily_task() + "\n",
             isAtAll=True)

