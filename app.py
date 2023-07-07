import requests
import os

url = "https://chat.openai.com/share/d312c52c-fe55-44a1-8f0d-f8547f74f36f"  # 你想要下载的网页的 URL
response = requests.get(url)

# 检查请求是否成功，HTTP 状态码 200 表示成功
if response.status_code == 200:
    web_content = response.text
    print(web_content)
else:
    print("Failed to download the page.")

with open(os.path.join("test2", url.split("/")[-1]), 'wb') as f:
    f.write(response.content)
