from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# 配置要访问的流量服务的URL和Authorization头
TRAFFIC_URL = "http://sp.2001817.xyz:18881/traffic"
AUTHORIZATION = "eff5ba3a-46c6-4fe6-9e03-4cddcc6ec03c"

# 字节转换函数
def convert_bytes(bytes):
    if bytes < 1024:
        return f"{bytes} B"
    kb = bytes / 1024
    if kb < 1024:
        return f"{kb:.2f} KB"
    mb = kb / 1024
    if mb < 1024:
        return f"{mb:.2f} MB"
    gb = mb / 1024
    if gb < 1024:
        return f"{gb:.2f} GB"
    tb = gb / 1024
    return f"{tb:.2f} TB"

@app.route('/traffic', methods=['GET'])
def get_traffic():
    try:
        # 从流量服务获取数据
        headers = {'Authorization': AUTHORIZATION}
        response = requests.get(TRAFFIC_URL, headers=headers)
        response.raise_for_status()  # 如果请求失败，抛出异常

        data = response.json()
        tx_bytes = data.get('user', {}).get('tx', 0)
        rx_bytes = data.get('user', {}).get('rx', 0)

        # 转换字节数
        tx_human_readable = convert_bytes(tx_bytes)
        rx_human_readable = convert_bytes(rx_bytes)

        # 返回JSON格式的响应
        return jsonify({
            'tx': tx_human_readable,
            'rx': rx_human_readable
        })

    except requests.RequestException as e:
        return jsonify({'error': 'Failed to fetch traffic data', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
