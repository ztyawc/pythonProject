# 导入相关库
import json
import hashlib
import base64
import hmac
import os
import time
import requests
from urllib.parse import quote_plus


# 构造函数生成timestamp和sign
def creat_sign(secret):
    timestamp = str(round(time.time() * 1000))
    se = secret.encode('utf-8')
    tse = '{}\n{}'.format(timestamp, secret)
    tsee = tse.encode('utf-8')
    hmac_code = hmac.new(se, tsee, digestmod=hashlib.sha256).digest()
    sign = quote_plus(base64.b64encode(hmac_code))

    return timestamp, sign

# 发送markdown消息
def send_md(title, text, Mobiles=None, UserIds=None, isAtAll=False):
    # 构造post参数
    url = "https://oapi.dingtalk.com/robot/send"
    headers = {'Content-Type': 'application/json'}
    timestamp, sign = creat_sign('SEC2309326f38745cfa49ca9cc01d7e9b7afc95c434ad304ad08f073c530f33716b')
    params = {
        'access_token': 'fc392f3a66f59852ccbd233170c3e5f0dc836d124fc8cfe263914bc1f65a8595',
        "sign": sign,
        "timestamp": timestamp
    }

    # 构造数据集
    data = {
        "at": {
            "atMobiles": Mobiles,
            "atUserIds": UserIds,
            "isAtAll": isAtAll
        },
        "markdown": {
            "title": title
            , 'text': text
        },
        "msgtype": "markdown"
    }

    # 发送消息
    requests.post(
        url=url,
        data=json.dumps(data),
        params=params,
        headers=headers
    )