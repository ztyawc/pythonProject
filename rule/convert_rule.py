# convert_openai_list.py

# 定义处理函数

def process_domain_suffix(domain_suffix):
    return f'domain:{domain_suffix}\n'

def process_domain(domain):
    return f'full:{domain}\n'

def process_domain_keyword(keyword):
    return f'{keyword}\n'

def process_ip_cidr(ip_cidr):
    return f'{ip_cidr}\n'

# 打开 TikTok.list 文件并读取内容
with open('rule/TikTok.list', 'r') as infile:
    # 读取所有行并存储在变量中
    lines = infile.readlines()

# 创建一个新的文件来写入转换后的内容
success = False
with open('rule/new_list_tiktok.txt', 'w') as outfile:
    # 遍历每一行
    for line in lines:
        # 去除行首尾空白字符
        line = line.strip()
        # 检查行的开头并进行相应的转换
        if line.startswith('DOMAIN-SUFFIX,'):
            domain_suffix = line.split(',')[1].strip()
            output = process_domain_suffix(domain_suffix)
            outfile.write(output)
            success = True
        elif line.startswith('DOMAIN,'):
            domain = line.split(',')[1].strip()
            output = process_domain(domain)
            outfile.write(output)
            success = True
        elif line.startswith('DOMAIN-KEYWORD,'):
            keyword = line.split(',')[1].strip()
            output = process_domain_keyword(keyword)
            outfile.write(output)
            success = True
        elif line.startswith('IP-CIDR,'):
            ip_cidr = line.split(',')[1].strip()
            output = process_ip_cidr(ip_cidr)
            outfile.write(output)
            success = True

# 根据处理结果输出信息
if success:
    print('转换成功')
else:
    print('没有进行任何转换')
