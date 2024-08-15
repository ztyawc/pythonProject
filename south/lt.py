import requests
import ding
url = "https://m.client.10010.com/servicequerybusiness/operationservice/queryOcsPackageFlowLeftContentRevisedInJune"
cookie=("ecs_acc=kIWBYZZjQKyN5QCbldViwRJlLFgwKx27WeUypXj3U+GzAVlde+KLKxD24X+HWuHEcTI2PedEh2CMrF0pkjzPO0rkW7uAh+yG5S8yAaIQQtuMKvFkXFvPwIe/NYKrPSfLUA9UVNKz4i98SJcluyBYGUqkBELTXFBiL1pqiCXrjvM=; "
        "ecs_token=eyJkYXRhIjoiYWVjZTQ5NTI5ZWVkODY0ZmNlMTA3NzdmODYxZDk3YTc2ZGYyOWRmOWVjY2I0ZWU4MGUwN2IxNzA4NDkxOTFkODEzNzNhMmE5ZWVkNWU5Yjg2NzBhYjcyZGNkZDRiYWVkZDc5ODFkZjViYWRjNTNlOWE5ZDE4N2ZmOWEwNGUxZTA2MmEzMDIwYWY1ZDQ0Mzc0M2QzODViZDIwZDc0ZGQ5M2M3ODQ5ZmJlMWRkZjVhMDBlOWE1Yzg3YjlmN2Q1MTI1NDZhNzM0ZWQ1ZTkwNTM1OTE4OTcwYWJhMmE2ZjA4OTNhODI3NGFmNmNiMzUwZTg5Mjc2MTU2ZjllYjI3ZDNhYmZhZTE2MzExNzUyMmJmMjkzYzJlNjQ1YmE2MzA5MjI0IiwidmVyc2lvbiI6IjAwIn0=")
headers = {
    "Host": "m.client.10010.com",
    "content-length": "137",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
    "accept": "application/json, text/plain, */*",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 14; 23127PN0CC Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.71 Mobile Safari/537.36; unicom{version:android@11.0702,desmobile:0};devicetype{deviceBrand:Real Manufacturer,deviceModel:Real Device}",
    "sec-ch-ua-platform": '"Android"',
    "origin": "https://img.client.10010.com",
    "x-requested-with": "com.sinovatech.unicom.ui",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://img.client.10010.com/",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie":cookie ,
    "priority": "u=1, i"
}

data = {
    "duanlianjieabc": "",
    "channelCode": "",
    "serviceType": "",
    "saleChannel": "",
    "externalSources": "",
    "contactCode": "",
    "ticket": "",
    "ticketPhone": "",
    "ticketChannel": "",
    "language": "chinese"
}

response = requests.post(url, headers=headers, data=data)

print(response.json()['RzbResources'][0]['details'][0])
#日租宝余量
day_addUpItemName=response.json()['RzbResources'][0]['details'][0]['feePolicyName']
day_remain=response.json()['RzbResources'][0]['details'][0]['remain']
day_use=response.json()['RzbResources'][0]['details'][0]['use']
print(response.json()['MlResources'][0]['details'][1])
m_use_gb = format(int(float(response.json()['MlResources'][0]['details'][1]['use'])) / 1024, ".2f")
print(m_use_gb)
print(response.json()['resources'][0]['details'][0])
r_addUpItemName=response.json()['resources'][0]['details'][0]['feePolicyName']
r_remain=response.json()['resources'][0]['details'][0]['remain']
r_use=response.json()['resources'][0]['details'][0]['use']
ding.send_md(title="联通流量监控", text="# 联通流量监控 \n ## •  类型：" + day_addUpItemName+"  已使用: "+day_use+"  剩余: "+day_remain
             +"\n"+" ## •  类型：" + r_addUpItemName+"  已使用: "+r_use+"  剩余: "+r_remain
             +"\n"+" ## •  类型：" + "免流"+"  已使用: "+m_use_gb+"Gb"
             , isAtAll=True)