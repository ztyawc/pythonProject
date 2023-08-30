import re
import requests
import ding

def get_cookies():
    headers = {
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
        return extracted_string

def sign():
    import requests

    cookies = {
        'think_language': 'zh-CN',
        'PHPSESSID': get_cookies(),
        'bjrcb_info': '04708D74644CD114E0E9CEE2B14222FE89EAC0CE1691F69B2838DD4CCFF6DD6133B302A6F20F3C771C1F801F1E9B019B1AFD4058B5EB26BF005C30040738F2365B458C8678483057D957ECBCF1F2484254FE30F5A2BD7FEF70CBA65CF954AEA7EB13332BC948B08EA646F5F5',
    }

    headers = {
        'Host': 'bjrcb.mocentre.cn',
        'Connection': 'keep-alive',
        # 'Content-Length': '44',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; M2012K11C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 App/BJRCB',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://bjrcb.mocentre.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://bjrcb.mocentre.cn/Wap/PolyPage/index?keymark=HdzqName&login_flag=1&Cid=04708D74644CD114E0E9CEE2B14222FE89EAC0CE1691F69B2838DD4CCFF6DD6133B302A6F20F3C771C1F801F1E9B019B1AFD4058B5EB26BF005C30040738F2365B458C8678483057D957ECBCF1F2484254FE30F5A2BD7FEF70CBA65CF954AEA7EB13332BC948B08EA646F5F5',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 'think_language=zh-CN; PHPSESSID=rvvrngvplar4kn2tm6lved24o3; bjrcb_info=04708D74644CD114E0E9CEE2B14222FE89EAC0CE1691F69B2838DD4CCFF6DD6133B302A6F20F3C771C1F801F1E9B019B1AFD4058B5EB26BF005C30040738F2365B458C8678483057D957ECBCF1F2484254FE30F5A2BD7FEF70CBA65CF954AEA7EB13332BC948B08EA646F5F5; public_ticket=ee7b2c7e4747425bf937f599b586fb19',
    }

    data = {
        'keymark': 'HdzqName',
        'game_key': 'qindao1',
        'todayTime': '',
    }

    response = requests.post('https://bjrcb.mocentre.cn/Wap/PolyPageSign/signIn', cookies=cookies, headers=headers,
                             data=data)
    return str(response.json()['msg'])



def lottery():
    cookies = {
        'think_language': 'zh-CN',
        'PHPSESSID': 'rvvrngvplar4kn2tm6lved24o3',
        'bjrcb_info': '04708D74644CD114E0E9CEE2B14222FE89EAC0CE1691F69B2838DD4CCFF6DD6133B302A6F20F3C771C1F801F1E9B019B1AFD4058B5EB26BF005C30040738F2365B458C8678483057D957ECBCF1F2484254FE30F5A2BD7FEF70CBA65CF954AEA7EB13332BC948B08EA646F5F5',
        'public_ticket': 'ee7b2c7e4747425bf937f599b586fb19',
        'jingqd0518_user': '%7B%22id%22%3A%22aC6Qg0Z3Wo7NcPZXV6IHYA%3D%3D%22%2C%22user_id%22%3A%220RILaEiBgVKSjJOCLmt3xw%3D%3D%22%2C%22user_name%22%3A%22%22%2C%22openid%22%3A%22%22%2C%22public_userid%22%3A%220%22%7D',
        'activity_ticket': '4c8a96d27a0d898c7b4479a005f2a6cd65583b1c',
        'shareUrl': '%2Findex.php%3Fm%3DWap%26c%3DLotteryDrawCommon%26a%3Dshare%26info%3DhqZzqbB6c9qxp3Gof3zVoZWOsaXGpNKees6ozoKLea6HzJ2psHqVk63Mp5qVe8quk6O4orKir6t_uI7fg6F5rYammaqxr3vWrdGGoYx3q256oKiwsLOnq363gth-pYauk7p8mMd-ntq-tnlne6Kkp5NomKW3p7ynitGP3n6gp52bqWtix32I3Mm4pJ2Xh6tueqPTqcWmyquLqHqWgouXnYWlfGLFaKbPxsx5Z3uhk66KaLmux4Gwn4q7g89-oKedkrmenaygocyxt4WamIWfdQ%26version%3D1',
        'jingqd0518_num': '1',
    }

    headers = {
        'Host': 'bjrcb.mocentre.cn',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; M2012K11C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 App/BJRCB',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://bjrcb.mocentre.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://bjrcb.mocentre.cn/index.php?m=Wap&c=LotteryDrawCommon&a=index&gameKey=jingqd0518&info=hqZzqbB6c9qxp3Gof3zVoZWOsaXGpNKees6ozoKLea6HzJ2psHqVk63Mp5qVe8quk6O4orKir6t_uI7fg6F5rYammaqxr3vWrdGGoYx3q256oKiwsLOnq363gth-pYauk7p8mMd-ntq-tnlne6Kkp5NomKW3p7ynitGP3n6gp52bqWtix32I3Mm4pJ2Xh6tueqPTqcWmyquLqHqWgouXnYWlfGLFaKbPxsx5Z3uhk66KaLmux4Gwn4q7g89-oKedkrmenaygocyxt4WamIWfdQ',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 'think_language=zh-CN; PHPSESSID=rvvrngvplar4kn2tm6lved24o3; bjrcb_info=04708D74644CD114E0E9CEE2B14222FE89EAC0CE1691F69B2838DD4CCFF6DD6133B302A6F20F3C771C1F801F1E9B019B1AFD4058B5EB26BF005C30040738F2365B458C8678483057D957ECBCF1F2484254FE30F5A2BD7FEF70CBA65CF954AEA7EB13332BC948B08EA646F5F5; public_ticket=ee7b2c7e4747425bf937f599b586fb19; jingqd0518_user=%7B%22id%22%3A%22aC6Qg0Z3Wo7NcPZXV6IHYA%3D%3D%22%2C%22user_id%22%3A%220RILaEiBgVKSjJOCLmt3xw%3D%3D%22%2C%22user_name%22%3A%22%22%2C%22openid%22%3A%22%22%2C%22public_userid%22%3A%220%22%7D; activity_ticket=4c8a96d27a0d898c7b4479a005f2a6cd65583b1c; shareUrl=%2Findex.php%3Fm%3DWap%26c%3DLotteryDrawCommon%26a%3Dshare%26info%3DhqZzqbB6c9qxp3Gof3zVoZWOsaXGpNKees6ozoKLea6HzJ2psHqVk63Mp5qVe8quk6O4orKir6t_uI7fg6F5rYammaqxr3vWrdGGoYx3q256oKiwsLOnq363gth-pYauk7p8mMd-ntq-tnlne6Kkp5NomKW3p7ynitGP3n6gp52bqWtix32I3Mm4pJ2Xh6tueqPTqcWmyquLqHqWgouXnYWlfGLFaKbPxsx5Z3uhk66KaLmux4Gwn4q7g89-oKedkrmenaygocyxt4WamIWfdQ%26version%3D1; jingqd0518_num=1',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    params = {
        'm': 'Wap',
        'c': 'LotteryDrawCommon',
        'a': 'lotteryResult',
        'info': 'hqZzqbB6c9qxp3Gof3zVoZWOsaXGpNKees6ozoKLea6HzJ2psHqVk63Mp5qVe8quk6O4orKir6t_uI7fg6F5rYammaqxr3vWrdGGoYx3q256oKiwsLOnq363gth-pYauk7p8mMd-ntq-tnlne6Kkp5NomKW3p7ynitGP3n6gp52bqWtix32I3Mm4pJ2Xh6tueqPTqcWmyquLqHqWgouXnYWlfGLFaKbPxsx5Z3uhk66KaLmux4Gwn4q7g89-oKedkrmenaygocyxt4WamIWfdQ',
        'version': '1',
    }

    response = requests.post('https://bjrcb.mocentre.cn/index.php', params=params, cookies=cookies, headers=headers)
    return str(response.json()['msg'])

strs=sign()
strl=lottery()

ding.send_md(title="测试", text="# 北京农商银行 \n ## •  签到："+strs+"\n## •  抽奖："+strl+"", isAtAll=True)