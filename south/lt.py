import os
import requests
import ding

url = "https://m.client.10010.com/servicequerybusiness/operationservice/queryOcsPackageFlowLeftContentRevisedInJune"

headers = {
    "Host": "m.client.10010.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://img.client.10010.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://img.client.10010.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "SHAREJSESSIONID=312F9070E818FB87AE1FA08D00B3A4E0; ecs_acc=; req_mobile=; req_serial=; req_wheel=ssss; acw_tc=1a0c65d017237739377188413e003b05fb5712d225c17fca0a0e84ac788dcd; arialoadData=false; city=019|; citycode=193; clientid=98|0; ecs_cook=7a96c526c8beccdfaa50adcacd8357cb; "
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
    "version": "WT",
    "userNumber": "",
    "language": "chinese"
}
response = requests.post(url, headers=headers, data=data)

print(response.json())
