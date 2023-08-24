import os


class IndexGenerator:
    def __init__(self):
        self.template = ""
        self.index_content = ""
        self.list_content = ""
        self.list_article = []
        self.init()

    def init(self):
        self.generate_article_list()
        self.generate_list_content2()
        self.generate_index_content()

    def generate(self):
        with open(f"index.html", 'w', encoding="utf-8") as f:
            f.write(self.index_content)

    def generate_article_list(self):
        article_list = []
        for dir_name in os.listdir(f"{os.getcwd()}"):
            dir_path = f"{os.getcwd()}/{dir_name}"
            if os.path.isdir(dir_path) and not dir_name.startswith("_") and not dir_name.startswith("."):
                local_li = ""
                for file_name in os.listdir(dir_path):
                    if file_name.endswith("html"):
                        base_name, ext = os.path.splitext(file_name)
                        article_obj = {
                            "title": base_name,
                            "date": "2020-01-01",
                            "category": dir_name
                        }
                        self.list_article.append(article_obj)

    def generate_list_content(self):
        # for dir_name in os.listdir(f"{os.getcwd()}"):
        #     dir_path = f"{os.getcwd()}/{dir_name}"
        #     if os.path.isdir(dir_path) and not dir_name.startswith("_") and not dir_name.startswith("."):
        #         local_li = ""
        #         for file_name in os.listdir(dir_path):
        #             if file_name.endswith("html"):
        #                 base_name, ext = os.path.splitext(file_name)
        #                 local_li += f"<li><a href='{dir_name}/{file_name}'>{base_name}</a></li> \n"
        #         self.list_content += f"<h2>{dir_name}</h2><ul>{local_li}</ul> \n"
        for article in self.list_article:
            self.list_content += (f"<li><a href='{article['category']}/{article['title']}.html'>{article['title']}</a"
                                  f"></li> \n")

    def generate_list_content2(self):
        for article in self.list_article:
            self.list_content += f"        <article><h3><a href='{article['category']}/{article['title']}.html'>{article['title']}</a></h3></article> \n"
            # self.list_content += (f"<li><a href='{article['category']}/{article['title']}.html'>{article['title']}</a"
            #                       f"></li> \n")

    def generate_index_content(self):
        with open(f"index.template", 'r', encoding="utf-8") as f:
            self.template = f.read()

        self.index_content = self.template.replace("%hook1%", self.list_content)


if __name__ == "__main__":
    IndexGenerator().generate()
    # print(IndexGenerator().list_article)
