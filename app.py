import os


class IndexGenerator:
    def __init__(self):
        self.template = ""
        self.index_content = ""
        self.list_category = ""
        self.list_content = ""
        self.list_article = []
        self.init()

    def init(self):
        self.generate_list_category()
        self.generate_article_list()
        self.generate_list_content2()
        self.generate_index_content()

    def generate(self):
        with open(f"index.html", 'w', encoding="utf-8") as f:
            f.write(self.index_content)

    def generate_article_list(self):
        for dir_name in os.listdir(f"{os.getcwd()}"):
            dir_path = f"{os.getcwd()}/{dir_name}"
            if os.path.isdir(dir_path) and not dir_name.startswith("_") and not dir_name.startswith("."):
                for file_name in os.listdir(dir_path):
                    if file_name.endswith("html"):
                        base_name, ext = os.path.splitext(file_name)
                        article_obj = {
                            "title": base_name,
                            "date": "2020-01-01",
                            "category": dir_name
                        }
                        self.list_article.append(article_obj)

    def generate_list_category(self):
        for dir_name in os.listdir(f"{os.getcwd()}"):
            dir_path = f"{os.getcwd()}/{dir_name}"
            if os.path.isdir(dir_path) and not dir_name.startswith("_") and not dir_name.startswith("."):
                self.list_category += f"            <li><a href='/category/tech'>{dir_name}</a></li>"
                self.list_category += "\n"

    def generate_list_content(self):
        for article in self.list_article:
            self.list_content += (f"<li><a href='{article['category']}/{article['title']}.html'>{article['title']}</a"
                                  f"></li> \n")

    def generate_list_content2(self):
        for article in self.list_article:
            self.list_content += "        <article>"
            self.list_content += f"<h3><a href='{article['category']}/{article['title']}.html'>{article['title']}</a></h3>"
            self.list_content += "<div class='post-metadata'>"
            self.list_content += f"<span class='category-tag'>{article['category']}</span>"
            self.list_content += f"<p class='post-date'>发布日期: {article['date']}</p>"
            self.list_content += "</div>"
            self.list_content += f"</article>"
            self.list_content += "\n"

    def generate_index_content(self):
        with open(f"index.template", 'r', encoding="utf-8") as f:
            self.template = f.read()
        self.index_content = self.template.replace("%category%", self.list_category)
        self.index_content = self.index_content.replace("%hook1%", self.list_content)


if __name__ == "__main__":
    IndexGenerator().generate()
    # print(IndexGenerator().list_article)
