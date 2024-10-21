#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : duanyan
# @email: duanyan2024@gmail.com
# @Time : 2024/10/20 下午10:00

from docx import Document
import pdfplumber


def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        content = []
        for page in pdf.pages:
            content.append(page.extract_text())
    return "\n".join(content)


def read_docx(file_path):
    # 打开 Word 文档
    document = Document(file_path)

    # 获取文档内容
    content = []
    for paragraph in document.paragraphs:
        content.append(paragraph.text)

    return "\n".join(content)


def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read(file_path) -> str:
    suffix = file_path.rsplit('.', 1)[1]
    if suffix == "txt":
        return read_txt(file_path)
    elif suffix == "pdf":
        return read_pdf(file_path)
    elif suffix == "docx":
        return read_docx(file_path)
    return ""



