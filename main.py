#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : duanyan
# @email: duanyan2024@gmail.com
# @Time : 2024/10/16 下午3:57

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from GPT import Chat
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from File import read


# 请提前在环境变量里设置api_key

FONT_DICT = dict()
FONT_INDEX = 1


class OpenAIApp:
    def __init__(self, root):
        self.__client = Chat()
        self.window = root
        self.window.title("OpenAI Chatbot")
        self.window.geometry("900x700")
        # 框体
        self.frame_chat = tk.Frame(root, bg='#549688')
        self.frame_chat.pack(expand=True, fill='both')
        """
        以下内容为frame_chat组件
        """
        # 标签-查询提示
        self.label_select = tk.Label(self.frame_chat, text="角色指定: ", font=("Microsoft YaHei", 16,),
                                     fg='#E4EAC5', bg='#549688')
        self.label_select.place(x=50, y=40)
        self.label_select = tk.Label(self.frame_chat, text="(Example: 你擅长使用python编程 )", font=("SimHei", 14, ),
                                     fg='black', bg='#549688')
        self.label_select.place(x=150, y=45)

        # 标签-查询提示
        self.label_select = tk.Label(self.frame_chat, text="输入文本以查询OpenAI:", font=("Microsoft YaHei", 16,),
                                     fg='#E4EAC5', bg='#549688')
        self.label_select.place(x=50, y=135)

        self.label_file = tk.Label(self.frame_chat, text="文件上传/清除文件内容", font=("SimHei", 14, ),
                                     fg='#E4EAC5', bg='#549688')
        self.label_file.place(x=540, y=150)

        # 标签-响应提示
        self.label_response = tk.Label(self.frame_chat, text="响应日志:", font=("Microsoft YaHei", 16,),
                                       fg='#E4EAC5', bg='#549688')
        self.label_response.place(x=50, y=260)

        # 按钮-提交
        self.button_submit = tk.Button(self.frame_chat, text="慢一点查哦", command=self.query_openai,
                                       takefocus=False,
                                       bd=5, relief="raised",  fg='#022A9B', bg='#FFCD06',
                                       font=("KaiTi", 24, "bold"))
        self.button_submit.place(x=600, y=190)
        # 按钮-文件上传
        self.content = ""
        self.has_file = False
        self.button_file = tk.Button(self.frame_chat, text="     ", command=self.file_upload,
                                       takefocus=False,
                                       bd=5, bg='#A4E2C6',
                                     font=("Microsoft YaHei", 8,),
                                     )
        self.button_file.place(x=780, y=140)

        # 按钮-历史刷新
        self.button_refresh = tk.Button(self.frame_chat, text="上下文刷新", command=self.__refresh_log, takefocus=False,
                                        bd=5, relief="raised", bg='#F4EAC5', font=("Microsoft YaHei", 12,))
        # self.button_refresh.place(x=600, y=125)

        # 文本框-背景
        self.input_back = scrolledtext.ScrolledText(self.frame_chat, wrap=tk.WORD, width=78, height=2,
                                                    font=("SimHei", 14,))
        self.input_back.place(x=50, y=75)

        # 文本框-问题输入
        self.input_text = scrolledtext.ScrolledText(self.frame_chat, wrap=tk.NONE, width=46, height=4,
                                                    font=("SimHei", 14,)
                                                    )
        self.input_text.place(x=50, y=175)

        # 文本框-响应
        self.response_text = scrolledtext.ScrolledText(self.frame_chat, wrap=tk.WORD, width=112, height=30)
        self.response_text.place(x=50, y=300)
        self.__font_type = "KaiTi"
        self.response_text.tag_config('common', font=(self.__font_type, 14, "normal"))
        self.__font_color = '#000000'
        self.__font_size = 6
        self.__title_mapping = [22, 20, 18, 16, 14, 14, 14]
        self.__is_title = False
        # 607D8B 455A64
        self.__font_style = "normal"
        self.__is_code = False

    # Openai查询
    def query_openai(self):
        # 从输入框获取用户输入
        user_input = self.input_text.get(index1="1.0", index2=tk.END)
        back_ground = self.input_back.get(index1="1.0", index2=tk.END)
        if back_ground:
            self.__client.update_log(back_ground, "system")
            self.input_back.delete("1.0", tk.END)
            self.response_text.insert(tk.END, f"\n系统: \n{back_ground}", "common"
                                      )

        if not user_input:
            return

        # 清空输入框
        self.input_text.delete("1.0", tk.END)

        # 执行OpenAI查询
        try:
            self.__client.update_log(user_input)
            if self.has_file:
                self.__client.update_log('以下是文件具体内容:')
                self.__client.update_log(self.content)
                self.content = ""
                self.has_file = False
            response = self.__client.chat(is_stream=True)
            answer = ""
            # 显示响应
            self.response_text.insert(tk.END, f"\nUser:\n {user_input}\nGPT: \n",  "common"
                                      )
            for chunk in response:
                text = chunk.choices[0].delta.content
                if text == None:
                    break
                # print([text])
                answer += text
                text = self.__parse(s=text)
                tup = (self.__font_type, (self.__title_mapping[self.__font_size]), self.__font_style)
                is_exist = OpenAIApp.find_key(tup)
                if is_exist == "":
                    global FONT_INDEX
                    is_exist = f"style_{FONT_INDEX}"
                    FONT_DICT[is_exist] = tup
                    self.response_text.tag_config(is_exist, font=tup)
                    FONT_INDEX += 1
                self.response_text.insert(tk.END, text, is_exist)
                self.response_text.yview(tk.END)
                self.response_text.update()
            self.__client.update_log(text=answer, role="assistant")
            # print(FONT_DICT)
        except Exception as e:
            self.response_text.insert(tk.END, f"Error: {str(e)}\n\n")
            self.response_text.update()

    def file_upload(self):
        if not self.has_file:
            file_path = filedialog.askopenfilename(title="不错，就在这里上传文件",
                                                   filetypes=[("PDF", "*.pdf"), ("DOCX", "*.docx"), ("TXT", "*.txt")])
            if file_path:
                try:
                    content = read(file_path)
                    messagebox.showinfo("文件上传", "鼠鼠收到了你的文件了捏！再次点击鼠鼠就扔了哦!")
                    self.content = content
                    self.has_file = True
                except Exception as e:
                    messagebox.showerror("Error", f"呜呜呜, 鼠鼠没收到文件: \n{e}")
        else:
            self.content = ""
            self.has_file = False
            messagebox.showinfo("文件上传", "鼠鼠把你的文件丢啦")

    # MarkDown解析
    def __parse(self, s):
        # 当前只解析1-6级标题, 加粗, 斜体, 代码块主体
        # TODO: 非标题`#`的解析
        s.replace(" ", "\u00A0")   # 解决中英文自动换行问题
        if not self.__is_code:
            if s == '#' or s == '##' or s == '###' or s == '####' or \
                    s == '#####' or s == '######':
                self.__is_title = True
                self.__font_size = len(s) - 1
                self.__font_style = 'bold'
                # if s == '######':
                #     self.__font_color = '#455A64'
                return ""
            elif s == " **":
                self.__font_style = "bold"
                return ""
            elif s == " *":
                self.__font_style = "italic"
                return ""
            elif s == "**" or s == '*':
                self.__font_style = "normal"
                return ""
            elif "\n" in s:
                self.__font_size = 6
                self.__font_style = "normal"
                if s == '**\n':
                    return '\n'
            elif s == '```':
                self.__is_code = True
                return ""
            if s == '`\n\n':
                return '\n\n'
            if self.__is_title:
                self.__is_title = False
                return s[1:]
        else:
            if s == '``':
                self.__is_code = False
                return ""
        return s

    def __refresh_log(self):
        self.__client.messages = []

    @staticmethod
    def find_key(tup):
        for key, value in FONT_DICT.items():
            if value == tup:
                return key
        return ""


def main():
    # 创建根窗口
    root = tk.Tk()
    OpenAIApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
