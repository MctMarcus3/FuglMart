class Comment:
    count_id = 0

    def __init__(self, content):
        Comment.count_id += 1
        self.__id = Comment.count_id
        self.__content = content
        self.__user = ''

    def get_id(self):
        return self.__id

    def get_content(self):
        return self.__content

    def set_content(self, content):
        self.__content = content


class Post(Comment):
    def __init__(self, title, content):
        self.__title = title
        self.__comments = []
        super().__init__(content)

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_comments(self):
        return self.__comments

    def add_comment(self, comment):
        self.__comments.append(comment)
