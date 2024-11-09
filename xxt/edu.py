import requests
import time
import ding
# 定义发送通知的函数

# 定义检查请求的函数
def check_activate_site():
    try:
        response = requests.post("https://activate.wctc.edu", timeout=5)
        if response.status_code == 200:
            print("成功")
            ding.send_md("通知", "activate.wctc.edu 已成功响应！")
    except requests.RequestException as e:
        print("请求失败:", e)


# 每秒执行一次检查
while True:
    check_activate_site()
    time.sleep(1)
