import re
import requests

def fb():
    cookies = {
        'think_language': 'zh-CN',
        'PHPSESSID': 'gjcsrrejd54fkmr5fhdr24orqa',
        'bjrcb_info': '04B4ED68F430C5C0EB0FC747913BA21B06B395FA476B3B211F1737507EC1C65DF6BCBCF7F5569CA6B17EDF9312D5DE8CC6AC02EBC970958D6802BA81D6BAA1D741168D3DDAA089CF6B9075693692AE1392FCC685B361F1AC8371DDED2DF54BB342025A1B095073292789943E',
    }

    headers = {
        'Host': 'bjrcb.mocentre.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; M2012K11C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 App/BJRCB',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'cn.com.bjns.mbank',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://bjrcb.mocentre.cn/Wap/PolyPage/index?keymark=HdzqName&login_flag=1&Cid=04B4ED68F430C5C0EB0FC747913BA21B06B395FA476B3B211F1737507EC1C65DF6BCBCF7F5569CA6B17EDF9312D5DE8CC6AC02EBC970958D6802BA81D6BAA1D741168D3DDAA089CF6B9075693692AE1392FCC685B361F1AC8371DDED2DF54BB342025A1B095073292789943E',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 'think_language=zh-CN; PHPSESSID=ak7q655p8c24ni7auceik34h7b; bjrcb_info=04B4ED68F430C5C0EB0FC747913BA21B06B395FA476B3B211F1737507EC1C65DF6BCBCF7F5569CA6B17EDF9312D5DE8CC6AC02EBC970958D6802BA81D6BAA1D741168D3DDAA089CF6B9075693692AE1392FCC685B361F1AC8371DDED2DF54BB342025A1B095073292789943E',
    }

    response = requests.get(
        'https://bjrcb.mocentre.cn/Wap/LotteryDrawCommon/index/alone/1/token/mocentreabc/lotteryKey/fenghuang1.html',
        cookies=cookies,
        headers=headers,
    )
    data = str(response.cookies)
    pattern = r'fenghuang1_user=(.*?) for'

    match = re.search(pattern, data)
    if match:
        variable_value = match.group(1)
        variable_value=str(variable_value)
        print(variable_value)
        return variable_value
    else:
        print("Variable not found.")

fb()