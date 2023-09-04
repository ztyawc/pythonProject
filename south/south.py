import requests
import ding
import xml.etree.ElementTree as ET

data = {'a': '', 'b': '', 'c': '', 'd': ''}


def daily_task():
    import datetime
    today = datetime.datetime.now().weekday()
    if today == 0:  # Monday
        URL = 'https://www.south-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job&cid=14&nowtime=1693814727224&verify=f0ad8f41'
        HEADERS = {
            'authority': 'www.south-plus.net',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'eb9e6_cknum=AwZcVw0CAFUNXDtqVlsJAgABCwRTVVMHUVRbAlYAUghcVgdQAQVcVQILV1U%3D; eb9e6_ck_info=%2F%09; eb9e6_winduser=AwdXUQMHAm0MAgVbAAoJVFdRVgQBUwFWAAILUVBXUA4PUAdUUVJXXDw%3D; eb9e6_ol_offset=80025; peacemaker=1; eb9e6_lastpos=other; eb9e6_lastvisit=87%091693814246%09%2Fplugin.php%3FH_name%3Dtasks%26action%3Dajax%26actions%3Djob%26cid%3D15%26nowtime%3D1693814245244%26verify%3Df0ad8f41',
            'referer': 'https://www.south-plus.net/plugin.php?H_name-tasks.html',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'iframe',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }

        def get_response():
            response = requests.get(URL, headers=HEADERS)
            root = ET.fromstring(response.text)

            # 获取<ajax>标签的文本内容
            cdata = root.text
            data['a'] = str(cdata)
            return cdata

        print(get_response())

        URL = 'https://www.south-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job2&cid=15&nowtime=1693821261321&verify=f0ad8f41'
        HEADERS = {
            'authority': 'www.south-plus.net',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'eb9e6_cknum=AwZcVw0CAFUNXDtqVlsJAgABCwRTVVMHUVRbAlYAUghcVgdQAQVcVQILV1U%3D; eb9e6_ck_info=%2F%09; eb9e6_winduser=AwdXUQMHAm0MAgVbAAoJVFdRVgQBUwFWAAILUVBXUA4PUAdUUVJXXDw%3D; peacemaker=1; eb9e6_lastpos=other; eb9e6_lastvisit=0%091693821252%09%2Fplugin.php%3FH_name-tasks-actions-newtasks.html.html; eb9e6_ol_offset=11252',
            'referer': 'https://www.south-plus.net/plugin.php?H_name-tasks-actions-newtasks.html.html',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'iframe',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }

        def get_response():
            response = requests.get(URL, headers=HEADERS)
            root = ET.fromstring(response.text)

            # 获取<ajax>标签的文本内容
            cdata = root.text
            data['b'] = str(cdata)
            return cdata

        print(get_response())


daily_task()


def daily_task():
    URL = 'https://www.south-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job&cid=15&nowtime=1693814245244&verify=f0ad8f41'
    HEADERS = {
        'authority': 'www.south-plus.net',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'eb9e6_cknum=AwZcVw0CAFUNXDtqVlsJAgABCwRTVVMHUVRbAlYAUghcVgdQAQVcVQILV1U%3D; eb9e6_ck_info=%2F%09; eb9e6_winduser=AwdXUQMHAm0MAgVbAAoJVFdRVgQBUwFWAAILUVBXUA4PUAdUUVJXXDw%3D; eb9e6_ol_offset=80025; peacemaker=1; eb9e6_lastpos=other; eb9e6_lastvisit=69%091693814228%09%2Fplugin.php%3FH_name-tasks.html',
        'referer': 'https://www.south-plus.net/plugin.php?H_name-tasks.html',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    def get_response():
        response = requests.get(URL, headers=HEADERS)
        root = ET.fromstring(response.text)

        # 获取<ajax>标签的文本内容
        cdata = root.text
        data['c'] = str(cdata)
        return cdata

    print(get_response())

    URL = 'https://www.south-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job2&cid=15&nowtime=1693821261321&verify=f0ad8f41'
    HEADERS = {
        'authority': 'www.south-plus.net',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'eb9e6_cknum=AwZcVw0CAFUNXDtqVlsJAgABCwRTVVMHUVRbAlYAUghcVgdQAQVcVQILV1U%3D; eb9e6_ck_info=%2F%09; eb9e6_winduser=AwdXUQMHAm0MAgVbAAoJVFdRVgQBUwFWAAILUVBXUA4PUAdUUVJXXDw%3D; peacemaker=1; eb9e6_lastpos=other; eb9e6_lastvisit=0%091693821252%09%2Fplugin.php%3FH_name-tasks-actions-newtasks.html.html; eb9e6_ol_offset=11252',
        'referer': 'https://www.south-plus.net/plugin.php?H_name-tasks-actions-newtasks.html.html',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    def get_response():
        response = requests.get(URL, headers=HEADERS)
        root = ET.fromstring(response.text)

        # 获取<ajax>标签的文本内容
        cdata = root.text
        data['d'] = str(cdata)
        return cdata

    print(get_response())


daily_task()

ding.send_md(title="测试", text="# south: \n ## •  周：" + data['a'] + "\n## •  周：" + data[
    'b'] + "\n## •  天：" + data['c'] + "\n## •  天：" + data['d'] + "\n",
             isAtAll=True)
