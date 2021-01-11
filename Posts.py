class Posts:
    count_id = 0

    def __init__(self, title, content,):
        Posts.count_id += 1
        self.__posts_id = Posts.count_id
        self.__title = title
        self.__content = content

    def get_posts_id(self):
        return self.__posts_id

    def get_title(self):
        return self.__title

    def get_content(self):
        return self.__content


    def set_posts_id(self, posts_id):
        self.__posts_id = posts_id

    def set_title(self, title):
        self.__title = title

    def set_content(self, content):
        self.__content = content
