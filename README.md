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




