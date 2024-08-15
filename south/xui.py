import requests


import requests
import ding

Cookie= "lang=zh-Hans; session=MTcyMzQxODk4NHxEWDhFQVFMX2dBQUJFQUVRQUFCMV80QUFBUVp6ZEhKcGJtY01EQUFLVEU5SFNVNWZWVk5GVWhoNExYVnBMMlJoZEdGaVlYTmxMMjF2WkdWc0xsVnpaWExfZ1FNQkFRUlZjMlZ5QWYtQ0FBRUVBUUpKWkFFRUFBRUlWWE5sY201aGJXVUJEQUFCQ0ZCaGMzTjNiM0prQVF3QUFRdE1iMmRwYmxObFkzSmxkQUVNQUFBQUdmLUNGZ0VDQVFaNmRIbGhkMk1CQ1hwMGVURXlNelExTmdBPXxzhoT0rlTMAE1_FZpWspF94DELrSBRrNbm5PVggQSTuw=="


def getinfo():
    url = "http://jp.2001817.xyz:543/panel/inbound/list"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": Cookie,
        "Origin": "http://jp.2001817.xyz:543",
        "Referer": "http://jp.2001817.xyz:543/panel/inbounds",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    response = requests.post(url, headers=headers, verify=False)

    print(response.json()['obj'][1]['clientStats'][0])
    total=response.json()['obj'][1]['clientStats'][0]['total']
    up=response.json()['obj'][1]['clientStats'][0]['up']
    down=response.json()['obj'][1]['clientStats'][0]['down']
    print(up+down)

    url1 = "http://jp.2001817.xyz:543/panel/inbound/updateClient/9d68f3c6-c1b8-4501-be4f-eaf7ceb62c85"
    headers1 = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": Cookie,
        "Origin": "http://jp.2001817.xyz:543",
        "Referer": "http://jp.2001817.xyz:543/panel/inbounds",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    data1 = {
        "id": "3",
        "settings": '{"clients": [{"id": "9d68f3c6-c1b8-4501-be4f-eaf7ceb62c85", "flow": "", "email": "ih2u71xj", "limitIp": 0, "totalGB": '+str(total+85899345920)+', "expiryTime": 0, "enable": true, "tgId": "", "subId": "mrt6x26tn2fkz5i1", "reset": 0}]}'
    }
    remaining = up+down
    if ((total-remaining)>=85899345920):
        print("流量充足")
    else:
        response1 = requests.post(url1, headers=headers1, data=data1, verify=False)
        print(response1.json())
        ding.send_md(title="测试", text="# xui \n ## •  xui：" + str(response1.json()['msg']), isAtAll=True)

getinfo()