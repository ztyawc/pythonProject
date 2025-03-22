import requests
import re

def get_code(query):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://javdb.com/',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }

    cookies = {
        'list_mode': 'h',
        'theme': 'auto',
        'locale': 'zh',
        'over18': '1',
        '_ym_uid': '173312576641059203',
        '_ym_d': '1733125766',
        'redirect_to': '/v/XYNpV',
        '_rucaptcha_session_id': '5f523cb72ca48e06e3d91731b074be9e',
        'cf_clearance': 'W3a1JcvkMZsZDEP.2N0I41lqBfTuLsElbmVXnRn_jVM-1742623437-1.2.1.1-vCAfOl9Tf3M7FwFpcesFqvFFQ6ewv77QiQ8SiUu6P6I8KAHC9cypIbleK1_nZDVOI2_KUwoFZmQKxWhps4EK71guLKdiaf061wTSR0PPP15CJIr4XTSxURfdUhNge9IAHbaBRvstaqMZotqRYnmwtni6vPFCVxPZ9P3tlXsFPn4.NeOQdccjKUMIsjsSKO6aoFEDO_NPxeuml.rsVJoluO1lf8ELUEg3F_ChaagK4YdEvRE5iGWIpbTwlfEqWRv2gPUaNv2U1ZpBxKZviAwzxbWSq7lg2CgBU92dEBDppIxu62tzARyXJuRQwae4PLSJZpWJz9TYq2aStMCmtGTfhwJykjOI52WUF63ik8tYlVI',
        '_jdb_session': 'eTYUrfzZb5SVK%2BzxdDfQl%2FXhNpmvl%2BndYtkHyYthDynt2WcEAJTjqMUmGEwEgWwvY0nZmaBU4lWe6RsVBSik3tTzAI%2BW6J9%2ByqrOLRykYXdWJD6Fh1b7Nkx0ZkI6tjXLseOMi6B08lKgdB8eobCp%2BHFVutCXffILD8YOHRJCuDGQoZr%2FuaJrIatPQI2kgIICPM%2BIgMXH9%2FPgtmsiGg0fEfK02qurA3D987XPthik1SLsLl5haAPOZ2Rixh6JHTvtPOlOGCVfgIKxXywWfWuzSZpfHj1KoqHmDVSYTMwhmZHwKfKijQ5XfofLE81rJRIALq0D0eXoBvW9R1kMkFPKwe7H%2BoQSS10Swh4Xv8ZTxTqwjHOY%2FBDmk3t6N%2FiGctVCXaA%3D--0I2SBp2Cqn%2BvSzzQ--cI13NcV0B%2Fi5IAj3W5UxaQ%3D%3D'
    }

    url = 'https://javdb.com/search'
    params = {
        'q': query,
        'f': 'all'
    }

    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response.status_code)

    # 从响应内容中提取代码
    content = response.text
    code_match = re.search(r'href="/v/([^"]+)"', content)
    if code_match:
        code = code_match.group(1)
        print(f'提取到的代码: {code}')
        return code
    else:
        print('未找到代码')
        return None

def parse_magnet_details(html_content):
    # 使用正则表达式提取磁力链接信息
    magnet_items = re.findall(r'<div class="item columns is-desktop[^"]*">.*?<div class="date column">', html_content, re.DOTALL)
    
    print("\n=== 磁力链接详情 ===")
    for item in magnet_items:
        # 提取名称
        name_match = re.search(r'<span class="name">(.*?)</span>', item)
        name = name_match.group(1) if name_match else "未知名称"
        
        # 提取大小和文件数
        meta_match = re.search(r'<span class="meta">\s*(.*?)\s*</span>', item)
        meta = meta_match.group(1) if meta_match else ""
        
        # 提取文件大小
        size_match = re.search(r'(\d+\.?\d*[GM]B)', meta)
        size = size_match.group(1) if size_match else ""
        
        # 提取文件数
        files_match = re.search(r'(\d+)個文件', meta)
        files = files_match.group(1) if files_match else ""
        
        # 提取日期
        date_match = re.search(r'<span class="time">(.*?)</span>', item)
        date = date_match.group(1) if date_match else ""
        
        # 提取标签
        tags = []
        if '高清' in item:
            tags.append('高清')
        if '字幕' in item:
            tags.append('字幕')
        if '无码破解' in item:
            tags.append('无码破解')
            
        # 提取磁力链接
        magnet_match = re.search(r'href="(magnet:\?xt=urn:btih:[^"]+)"', item)
        magnet = magnet_match.group(1) if magnet_match else ""
        
        # 打印详细信息
        print(f"\n文件名: {name}")
        if size:
            print(f"文件大小: {size}")
        if files:
            print(f"文件数量: {files}个")
        if date:
            print(f"发布日期: {date}")
        if tags:
            print(f"特征: {', '.join(tags)}")
        print(f"磁力链接: {magnet}")
        print("-" * 50)

def get_video_page(code):
    url = f'https://javdb.com/v/{code}'
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://javdb.com/search?q=ipx-811&f=all',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }
    
    cookies = {
        'list_mode': 'h',
        'theme': 'auto',
        'locale': 'zh',
        'over18': '1',
        '_ym_uid': '173312576641059203',
        '_ym_d': '1733125766',
        'redirect_to': '/v/XYNpV',
        '_rucaptcha_session_id': '5f523cb72ca48e06e3d91731b074be9e',
        'cf_clearance': 'BxLHOZuRZYX7Vzc4sc5rvb7RQ8GWY0Joi0g3tX2Fcj4-1742626464-1.2.1.1-O3nQGabYTlZ9TYxXeVCGvvNo7uW_xNMIVifZCi901BE5U6pEHKAlhSyNJyuR4uk5cCuT1.7eD2Q9ot7j1CcP8CVkHHazjs2710pZWxCbueSigi5I9hhedoNGLi4SM..ydrthuZrnESKXMs.SLtszvYCcC6IlyBEPDQQzm8tDt68VzqVZTbl1Xs9RRPrl7Ktd3ppAUdqnaKq2zXbGGe3nPb2INurqWBi4m9bK4pWAj8bDLwc1mIawmw1zlwCgpE53DrM3BnVrQ.YgwFvpxVZum.s0Aug4G7oVbIzeg1k3rEoKznXgtnkK149UVX3iFOGNUZ_W4pYvtjn0I.vGc_ML3D87m5GzlmBtF4bbJgImZVI',
        '_jdb_session': '6zGNMF240NQh9iRVlWtDkYSJVCodkOW1e%2BOymCDK96qzvZ%2Bm2YWKDEQOq6Sw7f1VbnFNFTPGls10%2Bw%2FNS31ItQ3L6sJa7M1yOtj7eDKP6YaVnDakIeZbwMwOJ9nJj7XuRWGd3XQYfHw%2BWXYFBewTPajyFVhVDKwhsQEEFjW9NW%2BysjRm3VIcDjSJqLq9zTsXGdMaeSHN1zp%2BsMqDER9W9yi7A3J8v230veS5LI4L%2BR%2Bbft8TyRKOCEsoz6OPvszTBjLOZkxWPakhDA65VmnW4qEiKaUJTL%2BcpoWeo0PgsfJVTEGjw6WLSJLtpfwLxxiM%2BInQcxwuJoYkHypkbWXltmioEMfK%2FKDQs8nCAdodpbYx8D2NzaoThCtSPHV4vw4eFaw%3D--svRVLepye80mi3Tv--btuAh8QY9qBSlI%2FJKF0RnA%3D%3D'
    }
    
    response = requests.get(url, headers=headers, cookies=cookies)
    print(f'Status code: {response.status_code}')
    content = response.text
    parse_magnet_details(content)
    return content

if __name__ == '__main__':
    get_video_page(get_code('ipzz-508'))