import requests
import xml.etree.ElementTree as ET
from notify import send

# 常量配置
BASE_URL = 'https://south-plus.net/plugin.php'
COMMON_HEADERS = {
    'authority': 'south-plus.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'eb9e6_cknum=CAMDAgBfAQYFCTtqDAQCAQQOWAIABlQHDQUIAFBTAQVUWlAPWAICVVICAQQ%3D; eb9e6_ck_info=%2F%09; eb9e6_winduser=CAMBAwdSAj9WAFdUAFICXFVdCFFXDlBXAAICAwACAVFRCAQIWlUABDg%3D; eb9e6_ol_offset=171108; peacemaker=1; eb9e6_lastpos=other',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

TASK_CONFIG = {
    'daily': {'cid': 15, 'name': '天'},
    'weekly': {'cid': 14, 'name': '周'}
}

def make_request(action, cid, verify='94a180c7'):
    """发送请求并解析响应"""
    try:
        params = {
            'H_name': 'tasks',
            'action': 'ajax',
            'actions': action,
            'cid': cid,
            'nowtime': 1704195091299,
            'verify': verify
        }
        
        response = requests.get(BASE_URL, headers=COMMON_HEADERS, params=params)
        response.raise_for_status()
        
        root = ET.fromstring(response.text)
        return root.text.split('\t')[1]
    except requests.RequestException as e:
        return f"请求失败: {str(e)}"
    except (ET.ParseError, IndexError) as e:
        return f"解析失败: {str(e)}"

def execute_task(task_type, is_complete=False):
    """执行任务"""
    action = 'job2' if is_complete else 'job'
    cid = TASK_CONFIG[task_type]['cid']
    return make_request(action, cid)

def main():
    """主函数"""
    results = []
    for task_type in ['weekly', 'daily']:
        task_name = TASK_CONFIG[task_type]['name']
        # 获取任务状态
        status = execute_task(task_type)
        results.append(f"## •  {task_name}：{status}")
        # 完成任务
        complete_status = execute_task(task_type, True)
        results.append(f"## •  {task_name}：{complete_status}")
    
    # 发送通知
    content = "# south: \n" + "\n".join(results) + "\n"
    send(title="签到信息", content=content)

if __name__ == "__main__":
    main()