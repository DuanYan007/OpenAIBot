#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : duanyan
# @email: duanyan2024@gmail.com
# @Time : 2024/10/16 下午7:40

from openai import OpenAI



class Chat:
    def __init__(self):
        self.messages = []
        self.model = "gpt-4o"
        self.client = OpenAI()

    def chat(self, is_stream=True):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=is_stream
        )
        """
        # 如果不需要Stream响应的话
                if not is_stream:
                   return response.choices[0].message.content
        """
        return response

    def update_log(self, text="", role="user"):
        # text = "说明加密解密原理"
        self.messages.append({"role": role, "content": text})
        if len(self.messages) > 20:
            self.messages = self.messages[-10:]


