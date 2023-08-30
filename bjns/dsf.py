
# -*- coding: utf-8 -*-
import requests
import json


def push_report(web_hook):
    # 定时任务触发钉钉报告推送
    key_word = "SEC2309326f38745cfa49ca9cc01d7e9b7afc95c434ad304ad08f073c530f33716b"

    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    message_body = {
        "msgtype": "markdown",
        "markdown": {
            "title": key_word,
            "text": "#### %s \n" % "消息推送展示项目：钉钉" +
                    "##### •  环境：测试环境 \n" +
                    "##### •  类型：%s \n" % "消息推送" +
                    "##### •  测试结果：%s \n" % "通过"
        },
        "at": {
            "atMobiles": [],
            "isAtAll": False
        }
    }
    send_data = json.dumps(message_body)  # 将字典类型数据转化为json格式
    ChatBot = requests.post(url=web_hook, data=send_data, headers=header)
    opener = ChatBot.json()
    if opener["errmsg"] == "ok":
        print(u"%s 通知消息发送成功！" % opener)
    else:
        print(u"通知消息发送失败，原因：{}".format(opener))


if __name__ == '__main__':
    # webhook 来自于 获取机器人webhook：复制webhook 中的那个值
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=fc392f3a66f59852ccbd233170c3e5f0dc836d124fc8cfe263914bc1f65a8595"
    push_report(webhook)