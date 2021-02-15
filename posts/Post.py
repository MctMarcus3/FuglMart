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

    def set_title(self, title):
        self.__title = title

    def set_content(self, content):
        self.__content = content

    def get_votecount(self):
        return self.__votecount


class Post(Comment):
    def __init__(self, title, content):
        super().__init__(title, content)
        self.comments = []

    def get_title(self):
        return self.__title

    def get_comments(self):
        return self.comments

    def set_title(self, title):
        self.__title = title

    def add_comment(self, comment):
        self.comments.append(comment)
