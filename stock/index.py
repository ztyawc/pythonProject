import requests
from datetime import datetime
import time

# Define the H2 cookie
H2_COOKIE = 'lang=zh-CN; 3x-ui=MTczMjI3MzQyN3xEWDhFQVFMX2dBQUJFQUVRQUFCMV80QUFBUVp6ZEhKcGJtY01EQUFLVEU5SFNVNWZWVk5GVWhoNExYVnBMMlJoZEdGaVlYTmxMMjF2WkdWc0xsVnpaWExfZ1FNQkFRUlZjMlZ5QWYtQ0FBRUVBUUpKWkFFRUFBRUlWWE5sY201aGJXVUJEQUFCQ0ZCaGMzTjNiM0prQVF3QUFRdE1iMmRwYmxObFkzSmxkQUVNQUFBQUdmLUNGZ0VDQVFaNmRIbGhkMk1CQ1hwMGVURXlNelExTmdBPXzjVnLpP5jc2Wm9EW5U5kn4Z88NgIJw8lPsmRrlo7KtQA=='
def addClient(base_url):
    client_id = input("请输入客户端ID: ")
    client_uuid = input("请输入客户端UUID: ")
    email = input("请输入客户端邮箱: ")
    expiry_date_str = input("请输入到期时间（格式为 YYYY-MM-DD）: ")

    # 将输入的日期转换为时间戳格式
    expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
    expiry_time = int(time.mktime(expiry_date.timetuple())) * 1000  # 转换为时间戳
    sub_id = input("请输入订阅ID: ")

    url = f"{base_url}/panel/inbound/addClient"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': H2_COOKIE,
        'Origin': base_url,
        'Referer': f"{base_url}/panel/inbounds",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {
        'id': client_id,
        'settings': (
            '{"clients": [{"id": "' + client_uuid + '", "flow": "", "email": "' + email +
            '", "limitIp": 0, "totalGB": 0, "expiryTime": ' + str(expiry_time) +
            ', "enable": true, "tgId": "", "subId": "' + sub_id + '", "reset": 0}]}'
        )
    }

    response = requests.post(url, headers=headers, data=data, verify=False)
    return response.json()

def listClients(base_url):
    url = f"{base_url}/panel/inbound/list"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': H2_COOKIE,
        'Origin': base_url,
        'Referer': f"{base_url}/panel/inbounds",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.post(url, headers=headers, verify=False)
    data = response.json()

    print(f"成功: {'是' if data['success'] else '否'}")
    print(f"消息: {data['msg'] if data['msg'] else '无'}")

    for obj in data['obj']:
        print("\n对象 ID:", obj['id'])
        print(f"  - 上行流量: {obj['up'] / 1_073_741_824:.2f} GB")
        print(f"  - 下行流量: {obj['down'] / 1_073_741_824:.2f} GB")
        if obj['total'] == 0:
            print("  - 总流量限制: 无限制")
        else:
            print(f"  - 总流量限制: {obj['total'] / 1_073_741_824:.2f} GB")
        print(f"  - 备注: {obj['remark']}")
        print(f"  - 启用状态: {'启用' if obj['enable'] else '禁用'}")
        print(f"  - 到期时间: {'无限期' if obj['expiryTime'] == 0 else obj['expiryTime']}")

        for client_stat in obj['clientStats']:
            print(f"    * 客户端 ID: {client_stat['id']}")
            print(f"    * 上行流量: {client_stat['up'] / 1_073_741_824:.2f} GB")
            print(f"    * 下行流量: {client_stat['down'] / 1_073_741_824:.2f} GB")

        print(f"  - 监听地址: {obj['listen'] if obj['listen'] else '无'}")
        print(f"  - 端口: {obj['port']}")
        print(f"  - 协议: {obj['protocol']}")

# Example usage:
base_url = 'http://94.159.108.242:543/a45xXffW0hNwYQQ'


response = listClients(base_url)

response = addClient(base_url)
print(response)