import requests
from datetime import datetime
import time

def addClient(base_url):
    client_id = input("请输入客户端ID: ")
    client_uuid = input("请输入客户端UUID: ")
    email = input("请输入客户端邮箱: ")
    expiry_date_str = input("请输入到期时间（格式为 YYYY-MM-DD）: ")

    # 将输入的日期转换为时间戳格式
    expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
    expiry_time = int(time.mktime(expiry_date.timetuple()))*1000  # 转换为时间戳
    sub_id = input("请输入订阅ID: ")

    url = f"{base_url}/panel/inbound/addClient"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'lang=zh-CN; 3x-ui=MTczMjI2OTY5NXxEWDhFQVFMX2dBQUJFQUVRQUFCMV80QUFBUVp6ZEhKcGJtY01EQUFLVEU5SFNVNWZWVk5GVWhoNExYVnBMMlJoZEdGaVlYTmxMMjF2WkdWc0xsVnpaWExfZ1FNQkFRUlZjMlZ5QWYtQ0FBRUVBUUpKWkFFRUFBRUlWWE5sY201aGJXVUJEQUFCQ0ZCaGMzTjNiM0prQVF3QUFRdE1iMmRwYmxObFkzSmxkQUVNQUFBQUdmLUNGZ0VDQVFaNmRIbGhkMk1CQ1hwMGVURXlNelExTmdBPXxBGPCdctxq6tTMMF7l7Ju43rwVcIet1XFls3rYW73FCw==',
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

# Example usage:
base_url = 'http://94.159.108.242:543/a45xXffW0hNwYQQ'
response = addClient(base_url)
print(response)