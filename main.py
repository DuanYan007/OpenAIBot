#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : duanyan
# @email: duanyan2024@gmail.com
# @Time : 2024/10/16 下午3:57

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from GPT import Chat

# 请提前在环境变量里设置api_key


class OpenAIApp:
    def __init__(self, root, client):
        self.client = client
        self.root = root
        self.root.title("OpenAI Chatbot")
        self.root.geometry("800x700")

        # 标签-查询提示
        self.label_select = ttk.Label(root, text="输入文本以查询OpenAI:", font=("Arial", 12))
        self.label_select.place(x=50, y=50)

        # 标签-响应提示
        self.label_response = ttk.Label(root, text="响应日志:", font=("Arial", 12))
        self.label_response.place(x=50, y=250)

        # 文本输入栏-问题输入
        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=10)
        self.input_text.place(x=50, y=75)

        # 按钮-提交
        self.submit_button = ttk.Button(root, text="提交", command=self.query_openai, takefocus=False)
        self.submit_button.place(x=650, y=225)

        # 文本框-响应
        self.response_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
        self.response_text.place(x=50, y=300)
        self.response_text.tag_config('large', font=("Arial", 18))
        self.response_text.tag_config('mid', font=("Arial", 16))
        self.response_text.tag_config('common', font=("Arial", 12))
        self.font = 'common'

    def query_openai(self):
        # 从输入框获取用户输入
        user_input = self.input_text.get(index1="1.0", index2=tk.END)
        if not user_input:
            return

        # 清空输入框
        self.input_text.delete("1.0", tk.END)

        # 执行OpenAI查询
        try:
            self.client.update_log(user_input)
            response = self.client.chat(is_stream=True)
            answer = ""
            # 显示响应
            self.response_text.insert(tk.END, f"\nUser:\n {user_input}\nGPT: \n", self.font)
            for chunk in response:
                text = chunk.choices[0].delta.content
                if text == None:
                    break
                answer += text
                text = self.parse(text)
                self.response_text.insert(tk.END, text, self.font)
                self.response_text.yview(tk.END)  # 滚动到底部
                self.response_text.update()
            self.client.update_log(text=answer, role="assistant")
        except Exception as e:
            self.response_text.insert(tk.END, f"Error: {str(e)}\n\n")
            self.response_text.update()

    def parse(self, string):
        if string == '###':
            self.font = "large"
            return ""
        elif string == "####":
            self.font = "mid"
            return ""
        elif "\n" in string:
            self.font = "common"
        return string


def main():
    # 创建根窗口
    client = Chat()
    root = tk.Tk()
    OpenAIApp(root, client)
    root.mainloop()


if __name__ == "__main__":
    main()