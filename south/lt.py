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
    "Cookie": "SHAREJSESSIONID=312F9070E818FB87AE1FA08D00B3A4E0; ecs_acc=; req_mobile=; req_serial=; clientid=98|0; req_wheel=ssss; mallcity=19|190; userprocode=019; selectedProvince=019; arialoadData=false; acw_tc=1a0c655417237402606605926e003d8ba6fa3350a3af999b94acec09a96658; ecs_cook=7a96c526c8beccdfaa50adcacd8357cb; unicomMallUid=2DVHfE11pXokoqB; JUT=nVVjwYRhiKXndK4OhyXhkeyEx2YwhY1uVa2VqKD0Qneh9/spXb/CfYnIlrh8NhBXSjbx0gUqFdhGIGJhievzSPLdo8fCkHxkT37Ytvy/wIUPxT5l8UOEq4qG6zoMex5/UzUE/K0M7NkcIkpl6XEP8V+97LpDQyPRuWipTtG2Z8yoMNmBzwWWRg1rcs7HSYLPVVDDaCkMPIMu6RM+lzXPnFABF80YO52KOd9HN+gqtbVAha1iOziYlpn4qDgQEHmnQjs262zzFZFZKqATp6dq/KyXWpYg8D3I07W8j+WSBGwoEi5FMzg/usHbiFmrFjhDafaPhVy4CiPy+xnwO/oFlGMRwHQ1kolKk71GMgt6qIhbjo94c0NJ+IOp7F+DHR4QhrJ3c8SjmkzbqwFnDTALXZDWyi7So/f0LFzb7wgP5Olq2ZLPoQ++x7ZAURy+pppS3K11RQ3IYXXdNM1MNE712OvTWUPly3TtAQs8kzpfx3q2ExaYXHBfSvKZW/Fhstdw2ubzsVTeqXPxLxrYZVQ/00c+CbO7xq/qMllUV+Mt1yMul/I3LsyZaSQ3XYFicW3LpTcQPMsQB6rUuuyQwIUYdnZKC4mn4uUZGX4CrZCmoSJErqGPWZ1JuYPVGuGVzLPVxuVH4UNLfdjA82vUTsez5Q==; piw=%%7B%%22login_name%%22%%3A%%22155****0817%%22%%2C%%22nickName%%22%%3A%%22155****0817%%22%%2C%%22rme%%22%%3A%%7B%%22ac%%22%%3A%%22%%22%%2C%%22at%%22%%3A%%22%%22%%2C%%22pt%%22%%3A%%2201%%22%%2C%%22u%%22%%3A%%2215536220817%%22%%7D%%2C%%22verifyState%%22%%3A%%22%%22%%7D; loginflag=true; citycode=193; u_account=xfRrzV%%252B%%252BZ17%%252FazcmXDyCvg%%253D%%253D; WT=155****0817; city=019|"
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

if (float(response.json()['RzbResources'][0]['rzbAllUse'])==0.0):
    day_addUpItemName="日租宝"
    day_remain = "0"
    day_use = float("0")
else:
    # 获取日租宝和其他流量使用量
    day_addUpItemName = response.json()['RzbResources'][0]['details'][0]['feePolicyName']
    day_remain = response.json()['RzbResources'][0]['details'][0]['remain']
    day_use = float(response.json()['RzbResources'][0]['details'][0]['use'])
r_use = float(response.json()['resources'][0]['details'][0]['use'])
# 获取其他资源的使用量和剩余量
m_use_gb = format(int(float(response.json()['MlResources'][0]['details'][1]['use'])) / 1024, ".2f")
r_addUpItemName = response.json()['resources'][0]['details'][0]['feePolicyName']
r_remain = response.json()['resources'][0]['details'][0]['remain']
# 文件路径
file_path_day = "day_use_data.txt"
file_path_r = "r_use_data.txt"

# 读取文件中的旧数据（如果存在）
if os.path.exists(file_path_day):
    with open(file_path_day, "r") as file:
        old_day_use = float(file.read().strip())
else:
    old_day_use = 0

if os.path.exists(file_path_r):
    with open(file_path_r, "r") as file:
        old_r_use = float(file.read().strip())
else:
    old_r_use = 0

# 判断是否有任何一个使用量增加超过10
if day_use > old_day_use + 10 or r_use > old_r_use + 10:
    # 发送消息
    ding.send_md(title="联通流量监控", text="# 联通流量监控 \n ## •  类型：" + day_addUpItemName + "  已使用: " + str(
        day_use) + "  剩余: " + day_remain
                                            + "\n" + " ## •  类型：" + r_addUpItemName + "  已使用: " + str(
        r_use) + "  剩余: " + r_remain
                                            + "\n" + " ## •  类型：" + "免流" + "  已使用: " + m_use_gb + "Gb"
                 , isAtAll=True)

# 将当前使用量写入文件
with open(file_path_day, "w") as file:
    file.write(str(day_use))

with open(file_path_r, "w") as file:
    file.write(str(r_use))


print("免流用量："+m_use_gb+"\n"+
      "日租宝已使用："+str(day_use)+   "   日租宝剩余："+(day_remain)+"\n"
      "免费1GB已使用："+str(r_use)+   "   免费1GB剩余："+(r_remain)
      )

