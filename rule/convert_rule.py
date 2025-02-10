# convert_openai_list.py

# 打开 OpenAI.list 文件并读取内容
with open('rule/OpenAI.list', 'r') as infile:
    # 读取所有行并存储在变量中
    lines = infile.readlines()

# 创建一个新的文件来写入转换后的内容
with open('rule/new_list.txt', 'w') as outfile:
    # 遍历每一行
    for line in lines:
        # 检查行的开头并进行相应的转换
        if line.startswith('DOMAIN-SUFFIX,'):
            # 提取域名后缀并写入
            domain_suffix = line.split(',')[1].strip()
            outfile.write(f'domain:{domain_suffix}\n')
            print(f'输出: domain:{domain_suffix}')
        elif line.startswith('DOMAIN,'):
            # 提取域名并写入
            domain = line.split(',')[1].strip()
            outfile.write(f'full:{domain}\n')
            print(f'输出: full:{domain}')
        elif line.startswith('DOMAIN-KEYWORD,'):
            # 提取关键字并写入
            keyword = line.split(',')[1].strip()
            outfile.write(f'{keyword}\n')
            print(f'输出: {keyword}')
        elif line.startswith('IP-CIDR,'):
            # 提取 IP 地址和 CIDR 部分并写入
            ip_cidr = line.split(',')[1].strip()
            outfile.write(f'{ip_cidr}\n')
            print(f'输出: {ip_cidr}')
