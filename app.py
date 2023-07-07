import requests
import os
from bs4 import BeautifulSoup


class ChatGPTDownloader:
    def __init__(self, url, category):
        self.url = url
        self.category = category
        self.type = type
        self.title = None
        self.content = None

    def download(self):
        response = requests.get(self.url)
        # 检查请求是否成功，HTTP 状态码 200 表示成功
        if response.status_code == 200:
            self.content = response.text
            self.content = self.content.replace("/_next/static", "../_next/static")
        else:
            print("Failed to download the page.")
        self.title = self.get_title()

    def get_title(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        # 查找 title 标签
        return soup.title.string

    def save(self):
        self.download()
        os.makedirs(self.category, exist_ok=True)
        with open(f"{self.category}/{self.title}.html", 'w', encoding="utf-8") as f:
            f.write(self.content)


class IndexGenerator:
    def __init__(self):
        self.template = ""
        self.index_content = ""
        self.list_content = ""
        self.init()

    def init(self):
        self.generate_list_content()
        self.generate_index_content()

    def generate(self):

        with open(f"index.html", 'w', encoding="utf-8") as f:
            f.write(self.index_content)

    def generate_list_content(self):
        for dir_name in os.listdir(os.getcwd()):
            if os.path.isdir(dir_name) and not dir_name.startswith("_") and not dir_name.startswith("."):
                local_li = ""
                for file_name in os.listdir(dir_name):
                    if file_name.endswith(".html"):
                        local_li += f"<li><a href='{dir_name}/{file_name}'>{file_name}</a></li> \n"
                self.list_content += f"<h2>{dir_name}</h2><ul>{local_li}</ul> \n"

    def generate_index_content(self):
        with open(f"index.template", 'r', encoding="utf-8") as f:
            self.template = f.read()

        self.index_content = self.template.replace("%hook1%", self.list_content)


if __name__ == "__main__":
    ChatGPTDownloader("https://chat.openai.com/share/0d64e6ad-71fd-4082-8f2f-e5ab25c92e05", "UE").save()
    # ChatGPTDownloader("https://chat.openai.com/share/d312c52c-fe55-44a1-8f0d-f8547f74f36f", "Linux").save()
    IndexGenerator().generate()

