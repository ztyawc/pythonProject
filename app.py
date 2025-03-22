from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__)

def get_code(query):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
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
    }

    url = 'https://javdb.com/search'
    params = {
        'q': query,
        'f': 'all'
    }

    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    content = response.text
    code_match = re.search(r'href="/v/([^"]+)"', content)
    if code_match:
        return code_match.group(1)
    return None

def parse_magnet_details(html_content):
    magnet_items = re.findall(r'<div class="item columns is-desktop[^"]*">.*?<div class="date column">', html_content, re.DOTALL)
    results = []
    
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
        
        results.append({
            'name': name,
            'size': size,
            'files': files,
            'date': date,
            'tags': tags,
            'magnet': magnet
        })
    
    return results

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
    }
    
    response = requests.get(url, headers=headers, cookies=cookies)
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if not query:
        return jsonify({'error': '请输入查询内容'})
    
    code = get_code(query)
    if not code:
        return jsonify({'error': '未找到相关内容'})
    
    content = get_video_page(code)
    magnets = parse_magnet_details(content)
    return jsonify({'magnets': magnets})

if __name__ == '__main__':
    app.run(debug=True) 