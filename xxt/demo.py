# 首先，我们设置起始和结束的questionLinkId
start_id = 884077565
end_id = 884076984

# 创建一个循环来遍历这些ID，并生成每个ID对应的URL
urls = []
for question_id in range(start_id, end_id - 1, -1):
    url = f"https://mooc1-api.chaoxing.com/exam-ans/exam/phone/look-detail?courseId=225542471&classId=99742884&examId=4912306&examAnswerId=124034377&isDetail=true&questionLinkId={question_id}&times=0&newVersion=1"
    urls.append(url)
    import requests
    from lxml import etree

    headers = {
        "Host": "mooc1-api.chaoxing.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23127PN0CC Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36(schild:297ad28341cc84a731e6c752c69a071f) (device:23127PN0CC) Language/zh_CN com.chaoxing.mobile/ChaoXingStudy_3_6.2.7_android_phone_1037_220 (@Kalimdor)_37db2f28bab1497c85cc22fbfeb17534",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh_CN",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://mooc1-api.chaoxing.com/exam-ans/exam/phone/look-detail?courseId=225556959&classId=89801283&examId=4139778&examAnswerId=110243722&cpi=349031619&newVersion=1&protocol_v=1",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": "k8sexam=1713450168.163.1241.15265; jrose=7615104434F749198419E76DA53F0C8C.mooc-exam-3958463579-j9gtf; lv=2; fid=10821; _uid=171324476; UID=171324476; vc=45D86F491B0AF78F3159F691B64507D1; xxtenc=da5a4fab2d61d3da24b1ceaf29609350; fidsCount=2; _industry=5; _tid=120715598; sso_puid=171324476; k8s=1713365171.745.83.386292; route=440ceb57420433374ff0504da9778fc7; uf=b2d2c93beefa90dcfa2942a530316ff4e26faa286893f2f24b4900953ce7c129efa75fad62cb442824c41b1813be9075428b5a98cdb27be888b83130e7eb470482d49b6a3665adad5b114e0781ae0d6c8487ca4cea3b44011899b42422f0aa5dbb640345aa3e85f0e7fafd565af53bf2; _d=1717501854625; vc2=54ED1BDE064464B6BF37706D0147E1D8; vc3=BfSLGlYRnJyjp03f5C0DwUbeUnSvUPIca%2F0P2pHVJjhnNfK7cIbqHpCtCy5IdG5FbJSin1FOZsKdWBs9Tc5DdsK9ZC4agg1lzU63IcRfvdyXPSB9zFDKGPkA6KYDX0YG93wZpdZsuH7xqWOWRPxjKmyk8Kn3gvjazr%2BAcG09mjg%3D4497dc1ce412c292578aea3fbc5bafbd; cx_p_token=60da4c7e524fe54553bb6ebd83bfeb5d; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIxNzEzMjQ0NzYiLCJsb2dpblRpbWUiOjE3MTc1MDE4NTQ2MjcsImV4cCI6MTcxODEwNjY1NH0.KNXbu4hyMpCa0I75No410K5WSQs5QVqggxgRN1jDrzY; DSSTASH_LOG=C_38-UN_10271-US_171324476-T_1717501854627; KI4SO_SERVER_EC=RERFSWdRQWdsckJiQXZ5ZmdkWW10cHVaZlp4MFBRSzFlZDRWZS8yVFduVGk3ci9Qc0Vpdlg3M1JJ%0AZkdBQU5LVkRtU2djWlRjU2NTVQp1NG13bWtscWxZSXhib1JIenZaTWMrazQwSElncjdRN3dlclJt%0ARDFtdWE0OVd4bXBHSTZoYnBwK2xKaTNmUjZCV1pORUt5NjNkRWxPCjhKbkRyZHlUUXBBN1YyMTRS%0AekU3MG96bjVhUU5ydk5OU3pNajNvY29hcU12bVBycExsckV6TWJLYkEvdFhVaTgwMTYzRHRKZUd2%0ARUgKaW55cFE3ZW1aNW9oUGRsVWp6SHVORHFmVXE1ZE8zaUxwSXhtQUdDNHhqSllPL3Q1STBLbUxW%0ASTBDK0ZjdUlETU1FSFVXTEFhM0lKSApsVldIKzhwUVhqQWxVR0hXTTN1VGh6VmJrblFqRXNucjB4%0ANmxoS2FWcXdnRGk1WTZxRUJYb29iMHFWTmIxeEIvZ1F1NCtMaUF6REJCCjFGaXdHdHlDUjVWVmgv%0AdktVRjR3SlZCaDF0S0Y0RlI4bFpQcy9nQ2dHcHc2MTVQandySXhEY1BUSFY2Y0NsdGoxQ2IrZHN6%0AbkV0Yk0KOUdrPT9hcHBJZD0xJmtleUlkPTE%3D; jrose=79A5C29D69A9171230CA1F16EBF8AF20.mooc-p4-2943247124-13tdl"    }
    response = requests.get(url, headers=headers)
    html_content = response.text

    # 解析HTML
    tree = etree.HTML(html_content)

    # 使用XPath定位到问题文本
    question_text = tree.xpath('//div[@class="tit"]/p/text()')

    print(question_text[0] if question_text else "问题未找到")
    file_name = 'output.txt'

    # 追加方式打开文件并写入提取的文本
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(str(question_id)+"   "+question_text[0] + '\n' if question_text else "问题未找到\n")

    # 选项
    # 使用XPath提取问题选项文本
    options = tree.xpath('//div[@class="optionBox"]/div[@class="optionCon"]/text()')

    # 要写入的文件名
    filename = "output.txt"

    # 将提取的文本写入文件
    with open(filename, "a", encoding="utf-8") as file:
        for option in options:
            file.write(option.strip() + "\n")
            print(option.strip())

    correct_answer = tree.xpath(
        "//div[contains(@class, 'answerCon border16')]/div[contains(@class, 'marBom40')]/div[@class='greenColor correctAnswer']/text()")

    # 输出正确答案
    if correct_answer:
        print("正确答案:", correct_answer[0].strip())
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write("正确答案:" + correct_answer[0] + '\n' if correct_answer else "问题未找到\n")
    else:
        print("未找到正确答案")

    # 将分隔符"--------------------------------"追加到文件末尾
    separator = "--------------------------------\n"

    # 打开文件并追加分隔符
    with open(file_name, 'a') as file:
        file.write(separator)

urls[:5]  # 显示前5个URL进行验证
