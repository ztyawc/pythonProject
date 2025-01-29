#!/usr/bin/env python3

import paramiko
import sys
import os
from notify import send
def ssh_connect():
    """
    连接到SSH服务器
    """
    # 固定的连接信息
    hostname = "s13.serv00.com"
    username = "ztyawc"
    password = os.getenv("SSH_PASSWORD")  # 请替换为实际密码
    port = 22

    try:
        # 创建SSH客户端实例
        ssh = paramiko.SSHClient()
        # 自动添加主机密钥
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # 使用密码认证
        ssh.connect(hostname, port, username, password)
        print(f"成功连接到 {hostname}")
        
        # 获取系统信息
        stdin, stdout, stderr = ssh.exec_command("uname -a")
        system_info = stdout.read().decode('utf-8')
        print(f"系统信息: {system_info}")
        send(title="SERV00", content=f"系统信息: {system_info}")
    except paramiko.AuthenticationException:
        print("认证失败，请检查密码")
    except paramiko.SSHException as ssh_exception:
        print(f"SSH异常: {ssh_exception}")
    except Exception as e:
        print(f"连接错误: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    ssh_connect()
