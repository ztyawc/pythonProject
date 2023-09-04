import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import random

def print_entry():
    text.insert(tk.END, entry.get() + '\n')

def calculate_birth_year():
    current_year = datetime.now().year
    birth_year = current_year - int(age_entry.get())
    text.insert(tk.END, '你是' + str(birth_year) + '年出生的\n')
    if age_entry.get() == '99':
        messagebox.showinfo("祝福", "祝您活到99岁")
        root.destroy()

def on_closing():
    if messagebox.askokcancel("退出", "你确定要退出吗?"):
        root.geometry(f'{random.randint(100, 1000)}x{random.randint(100, 1000)}')

root = tk.Tk()
root.title("图形化界面")
root.geometry('500x500')  # 调整窗口大小
root.protocol("WM_DELETE_WINDOW", on_closing)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)  # 增加内边距

left_frame = tk.Frame(frame)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)  # 增加内边距

right_frame = tk.Frame(frame)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)  # 增加内边距

entry = ttk.Entry(left_frame, width=30)  # 调整输入框大小
entry.pack(pady=10)  # 增加内边距

button = ttk.Button(left_frame, text="打印输入", command=print_entry)
button.pack(pady=10)  # 增加内边距

age_entry = ttk.Entry(left_frame, width=30)  # 调整输入框大小
age_entry.pack(pady=10)  # 增加内边距

age_button = ttk.Button(left_frame, text="计算出生年份", command=calculate_birth_year)
age_button.pack(pady=10)  # 增加内边距

text = tk.Text(right_frame, width=30, height=10)  # 调整文本框大小
text.pack(pady=10)  # 增加内边距

root.mainloop()





