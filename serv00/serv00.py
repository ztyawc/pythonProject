#!/usr/bin/env python3

import paramiko
import sys
import os
import logging
from time import sleep
from notify import send

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# SSH连接配置
SSH_CONFIG = {
    'hostname': 's13.serv00.com',
    'username': 'ztyawc',
    'password': os.getenv("SSH_PASSWORD"),  # 从环境变量获取密码
    'port': 22,
    'timeout': 10,
    'max_retries': 3
}

def notify(success: bool, message: str):
    """
    发送通知
    :param success: 是否成功
    :param message: 通知内容
    """
    try:
        status = "成功" if success else "失败"
        send(
            title=f"SERV00 连接{status}", 
            content=message
        )
    except Exception as e:
        logging.error(f"发送通知失败: {e}")

def ssh_connect():
    """SSH连接函数，包含重试机制"""
    if not SSH_CONFIG['password']:
        error_msg = "未设置SSH密码环境变量(SSH_PASSWORD)"
        logging.error(error_msg)
        notify(False, error_msg)
        return False

    for attempt in range(SSH_CONFIG['max_retries']):
        ssh = None
        try:
            # 创建SSH客户端实例
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # 连接服务器
            logging.info(f"正在尝试连接到 {SSH_CONFIG['hostname']} (尝试 {attempt + 1}/{SSH_CONFIG['max_retries']})")
            ssh.connect(
                hostname=SSH_CONFIG['hostname'],
                port=SSH_CONFIG['port'],
                username=SSH_CONFIG['username'],
                password=SSH_CONFIG['password'],
                timeout=SSH_CONFIG['timeout']
            )
            
            logging.info(f"成功连接到 {SSH_CONFIG['hostname']}")
            
            # 获取系统信息
            stdin, stdout, stderr = ssh.exec_command("uname -a")
            system_info = stdout.read().decode('utf-8').strip()
            error_info = stderr.read().decode('utf-8').strip()
            
            if error_info:
                raise Exception(f"命令执行错误: {error_info}")
            
            success_msg = f"连接成功\n系统信息: {system_info}"
            logging.info(success_msg)
            notify(True, success_msg)
            return True
            
        except paramiko.AuthenticationException:
            error_msg = "认证失败，请检查密码"
            logging.error(error_msg)
            notify(False, error_msg)
            return False
            
        except paramiko.SSHException as ssh_exception:
            error_msg = f"SSH异常: {ssh_exception}"
            logging.error(error_msg)
            if attempt < SSH_CONFIG['max_retries'] - 1:
                sleep(2)
                continue
            notify(False, error_msg)
            return False
            
        except Exception as e:
            error_msg = f"连接错误: {e}"
            logging.error(error_msg)
            if attempt < SSH_CONFIG['max_retries'] - 1:
                sleep(2)
                continue
            notify(False, error_msg)
            return False
            
        finally:
            if ssh:
                try:
                    ssh.close()
                except:
                    pass

def main():
    """主函数"""
    try:
        if ssh_connect():
            sys.exit(0)
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        error_msg = "用户中断执行"
        logging.info(f"\n{error_msg}")
        notify(False, error_msg)
        sys.exit(1)

if __name__ == "__main__":
    main()
