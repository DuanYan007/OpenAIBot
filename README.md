# OpenAIBot
#### **When you only have the api_key about the OpenAi, the OpenAIBot will help you use OpenAi more convinient**
#### **(当你只拥有OpenAi的api_key时， OpenAIBot将帮助你更方便地使用OpenAi)**
ps: 无法直连openai的，请设置全局代理
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
## 介绍以及使用细节(How to use)
- 支持长对话， 但有次数限制，不建议超过40，会影响访问速度，在GPT.py修改
- 支持上传文件, 仅局限于pdf, docx, txt, 无法解析图像
- 可提前指定系统的偏向(例如: 你擅长使用python编程)
- 支持GUI(pyhton tkinter实现)




