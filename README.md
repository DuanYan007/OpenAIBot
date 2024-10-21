# OpenAIBot
#### **When you only have the api_key about the OpenAi, the OpenAIBot will help you use OpenAi more convinient**
#### **(当你只拥有OpenAi的api_key时， OpenAIBot将帮助你更方便地使用OpenAi)**
ps: 无法直连openai的，请设置全局代理

ps：如有其他需求或bug, 可联系2907762730@qq.com
## 配置(Config)
### 1. 环境变量配置
cmd 操作(operation)
```cmd
setx OPENAI_API_KEY "your_api_key"
```
验证配置成功(validation)
```cmd
echo %OPENAI_API_KEY%
```
### 2. 依赖安装
```pip
pip install -r requirements.txt
```
```pip
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```
## 介绍以及使用(How to use)
- 支持长对话   (消息日志但有次数限制，不建议超过40，会影响访问速度，在GPT.py修改
- 支持上传文件 (仅局限于pdf, docx, txt后缀, 无法解析图像
- 支持markdown部分语法解析( 标题，加粗，斜体，代码块内部
- 支持GUI(python tkinter实现)
- 可提前指定系统的偏向(例如: 你擅长使用python编程
### exp1
![image](https://github.com/user-attachments/assets/83969fcf-061c-4bed-8c2f-58c15b56c2ce)
### exp2
![image](https://github.com/user-attachments/assets/29b6e719-69ee-41a6-97c2-4d2f3dadc8e0)
### exp3
![image](https://github.com/user-attachments/assets/5594104f-cf81-4ab1-a386-944662d5d27a)
### exp4
![image](https://github.com/user-attachments/assets/a6022207-f9b5-4d21-b0ec-922afe07d770)




# 祝大家生活愉快
