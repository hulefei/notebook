import os
import re
from datetime import datetime


class IndexGenerator:
    def __init__(self):
        self.template = ""
        self.index_content = ""
        self.list_category = ""
        self.list_dir = []
        self.list_article = []
        self.init()

    def init(self):
        self.init_dir_list()
        self.generate_list_category()
        self.generate_article_list()

    def generate(self):
        with open(f"index.html", 'w', encoding="utf-8") as f:
            f.write(self.generate_content(f"index"))

        for dir_name in self.list_dir:
            with open(f"{dir_name}.html", 'w', encoding="utf-8") as f:
                f.write(self.generate_content(f"{dir_name}"))

    def init_dir_list(self):
        for dir_name in os.listdir(f"{os.getcwd()}"):
            dir_path = f"{os.getcwd()}/{dir_name}"
            if os.path.isdir(dir_path) and not dir_name.startswith("_") and not dir_name.startswith("."):
                self.list_dir.append(dir_name)

    def generate_article_list(self):
        for dir_name in os.listdir(f"{os.getcwd()}"):
            dir_path = f"{os.getcwd()}/{dir_name}"
            if os.path.isdir(dir_path) and not dir_name.startswith("_") and not dir_name.startswith("."):
                for file_name in os.listdir(dir_path):
                    if file_name.endswith("html") or file_name.endswith("htm"):
                        pattern = r"^(\d{4}-\d{2}-\d{2}) (.*)\.[htm|html]"
                        # 使用search方法来查找匹配的字符串
                        match = re.search(pattern, file_name)
                        if match:
                            date_string = match.group(1)
                            title = match.group(2)
                            base_name, ext = os.path.splitext(file_name)
                            article_obj = {
                                "title": title,
                                "date": date_string,
                                "category": dir_name,
                                "ext": ext,
                            }
                            self.list_article.append(article_obj)
                        else:
                            # 将日期格式化为 YYYY-MM-DD 格式的字符串
                            date_string_2 = datetime.now().strftime('%Y-%m-%d')
                            base_name_2, ext_2 = os.path.splitext(file_name)
                            article_obj = {
                                "title": base_name_2,
                                "date": date_string_2,
                                "category": dir_name,
                                "ext": ext_2,
                            }
                            new_file_name = f"{date_string_2} {base_name_2}{ext_2}"
                            self.list_article.append(article_obj)
                            os.rename(f"{dir_path}/{file_name}", f"{dir_path}/{new_file_name}")

    def generate_list_category(self):
        for dir_name in self.list_dir:
            self.list_category += f"            <li><a href='{dir_name}.html '>{dir_name}</a></li>"
            self.list_category += "\n"

    @staticmethod
    def generate_list_content(articles):
        local_content = ""
        for article in articles:
            local_content += "        <article>"
            local_content += f"<h3><a href='{article['category']}/{article['date']} {article['title']}{article['ext']}'>{article['title']}</a></h3>"
            local_content += "<div class='post-metadata'>"
            local_content += f"<span class='category-tag'>{article['category']}</span>"
            local_content += f"<p class='post-date'>发布日期: {article['date']}</p>"
            local_content += "</div>"
            local_content += f"</article>"
            local_content += "\n"
        return local_content

    def generate_content(self, category):
        # filter self.list_article by category
        articles = [article for article in self.list_article if article["category"] == category or category == "index"]
        # sort self.generate_list_content by date
        articles.sort(key=lambda x: x["date"], reverse=True)
        with open(f"index.template", 'r', encoding="utf-8") as f:
            self.template = f.read()
        local_article = self.generate_list_content(articles)
        local_content = self.template.replace("%category%", self.list_category)
        local_content = local_content.replace("%article%", local_article)
        return local_content


if __name__ == "__main__":
    IndexGenerator().generate()
    # print(IndexGenerator().list_article)
