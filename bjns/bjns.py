import re
import time

import requests
import ding

list={'cook':'','check-in_status':'','Lottery_results':'','fbcj':'','fb':''}


gheaders = {
        'Host': 'bjrcb.mocentre.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; M2012K11C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 App/BJRCB',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'cn.com.bjns.mbank',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

def get_cookies(headers=gheaders):
    headers = headers

    params = {
        'keymark': 'HdzqName',
        'login_flag': '1',
        'Cid': '04708D74644CD114E0E9CEE2B14222FE89EAC0CE1691F69B2838DD4CCFF6DD6133B302A6F20F3C771C1F801F1E9B019B1AFD4058B5EB26BF005C30040738F2365B458C8678483057D957ECBCF1F2484254FE30F5A2BD7FEF70CBA65CF954AEA7EB13332BC948B08EA646F5F5',
    }

    response = requests.get('https://bjrcb.mocentre.cn/Wap/PolyPage/index', params=params, headers=headers)
    cookie_string = str(response.cookies)
    pattern = r'(?<=PHPSESSID=)([^;\s]+)'

    match = re.search(pattern, cookie_string)
    if match:
        extracted_string = match.group(1)
        print(extracted_string)
        extracted_string=str(extracted_string)
        list['cook']=extracted_string

def sign(headers=gheaders):
    import requests

    cookies = {
        'think_language': 'zh-CN',
        'PHPSESSID': list['cook'],
        'bjrcb_info': '04708D74644CD114E0E9CEE2B14222FE89EAC0CE1691F69B2838DD4CCFF6DD6133B302A6F20F3C771C1F801F1E9B019B1AFD4058B5EB26BF005C30040738F2365B458C8678483057D957ECBCF1F2484254FE30F5A2BD7FEF70CBA65CF954AEA7EB13332BC948B08EA646F5F5',
    }

    headers = headers

    data = {
        'keymark': 'HdzqName',
        'game_key': 'qindao1',
        'todayTime': '',
    }

    response = requests.post('https://bjrcb.mocentre.cn/Wap/PolyPageSign/signIn', cookies=cookies, headers=headers,
                             data=data)
    list['check-in_status']= str(response.json()['msg'])



def lottery():
    cookies = {
        'think_language': 'zh-CN',
        'PHPSESSID': list['cook'],
        'bjrcb_info': '04708D74644CD114E0E9CEE2B14222FE89EAC0CE1691F69B2838DD4CCFF6DD6133B302A6F20F3C771C1F801F1E9B019B1AFD4058B5EB26BF005C30040738F2365B458C8678483057D957ECBCF1F2484254FE30F5A2BD7FEF70CBA65CF954AEA7EB13332BC948B08EA646F5F5',
        'public_ticket': 'ee7b2c7e4747425bf937f599b586fb19',
        'jingqd0518_user': '%7B%22id%22%3A%22aC6Qg0Z3Wo7NcPZXV6IHYA%3D%3D%22%2C%22user_id%22%3A%220RILaEiBgVKSjJOCLmt3xw%3D%3D%22%2C%22user_name%22%3A%22%22%2C%22openid%22%3A%22%22%2C%22public_userid%22%3A%220%22%7D',
        'activity_ticket': '4c8a96d27a0d898c7b4479a005f2a6cd65583b1c',
        'shareUrl': '%2Findex.php%3Fm%3DWap%26c%3DLotteryDrawCommon%26a%3Dshare%26info%3DhqZzqbB6c9qxp3Gof3zVoZWOsaXGpNKees6ozoKLea6HzJ2psHqVk63Mp5qVe8quk6O4orKir6t_uI7fg6F5rYammaqxr3vWrdGGoYx3q256oKiwsLOnq363gth-pYauk7p8mMd-ntq-tnlne6Kkp5NomKW3p7ynitGP3n6gp52bqWtix32I3Mm4pJ2Xh6tueqPTqcWmyquLqHqWgouXnYWlfGLFaKbPxsx5Z3uhk66KaLmux4Gwn4q7g89-oKedkrmenaygocyxt4WamIWfdQ%26version%3D1',
        'jingqd0518_num': '1',
    }

    headers = gheaders

    params = {
        'm': 'Wap',
        'c': 'LotteryDrawCommon',
        'a': 'lotteryResult',
        'info': 'hqZzqbB6c9qxp3Gof3zVoZWOsaXGpNKees6ozoKLea6HzJ2psHqVk63Mp5qVe8quk6O4orKir6t_uI7fg6F5rYammaqxr3vWrdGGoYx3q256oKiwsLOnq363gth-pYauk7p8mMd-ntq-tnlne6Kkp5NomKW3p7ynitGP3n6gp52bqWtix32I3Mm4pJ2Xh6tueqPTqcWmyquLqHqWgouXnYWlfGLFaKbPxsx5Z3uhk66KaLmux4Gwn4q7g89-oKedkrmenaygocyxt4WamIWfdQ',
        'version': '1',
    }

    response = requests.post('https://bjrcb.mocentre.cn/index.php', params=params, cookies=cookies, headers=headers)
    list['Lottery_results']=str(response.json()['msg'])


def cj():

    cookies = {
        'think_language': 'zh-CN',
        'PHPSESSID': list['cook'],
        'fenghuang1_num': '0',
        'fenghuang1_user': '%7B%22id%22%3A%22aC6Qg0Z3Wo7NcPZXV6IHYA%3D%3D%22%2C%22user_id%22%3A%220RILaEiBgVKSjJOCLmt3xw%3D%3D%22%2C%22user_name%22%3A%22%22%2C%22openid%22%3A%22%22%2C%22public_userid%22%3A%220%22%7D',
    }

    headers = gheaders

    params = {
        'm': 'Wap',
        'c': 'LotteryDrawCommon',
        'a': 'decIntegralLottery',
        'alone': '1',
        'token': 'mocentreabc',
        'lotteryKey': 'fenghuang1',
    }

    response = requests.post('https://bjrcb.mocentre.cn/index.php', params=params, cookies=cookies, headers=headers)
    list['fbcj']=str(response.json()['msg'])
def cx():
    import requests

    cookies = {
        'think_language': 'zh-CN',
        'PHPSESSID': list['cook'],
        'bjrcb_info': '04744543D49DA3FF8A42E607BA9BFF7D70221CA88E4EF42FD95172EEFCBAAD9CD618F3136A94F503A626CA9ABDE3024E51E6B0D9DE7185B80AAFD720473B91CA99D59730FC340B7E7C9AA744625309CFAE787DB1BC0F12D350B268FD1E896B419214C03DE62B7FCFE5F3757B',
        'public_ticket': '7bf7e597b9a4fe1bee795d0283cbb2d6',
        'fenghuang1_user': '%7B%22id%22%3A%22aC6Qg0Z3Wo7NcPZXV6IHYA%3D%3D%22%2C%22user_id%22%3A%220RILaEiBgVKSjJOCLmt3xw%3D%3D%22%2C%22user_name%22%3A%22%22%2C%22openid%22%3A%22%22%2C%22public_userid%22%3A%220%22%7D',
        'fenghuang1_num': '1',
        'fenghuang1_num': '1',
    }

    headers = gheaders

    params = {
        'm': 'Wap',
        'c': 'LotteryDrawCommon',
        'a': 'lotteryResult',
        'alone': '1',
        'token': 'mocentreabc',
        'lotteryKey': 'fenghuang1',
    }

    response = requests.post('https://bjrcb.mocentre.cn/index.php', params=params, cookies=cookies, headers=headers)
    list['fb']=str(response.json()['msg'])
get_cookies()

sign()
lottery()
cj()
time.sleep(2)
cx()

ding.send_md(title="测试", text="# 北京农商银行 \n ## •  签到："+list['check-in_status']+"\n## •  抽奖："+list['Lottery_results']+"\n## •  翻倍抽奖状态："+list['fbcj']+"\n## •  翻倍抽奖奖品："+list['fb']+"\n", isAtAll=True)