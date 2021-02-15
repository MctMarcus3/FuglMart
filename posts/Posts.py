class Posts:
    count_id = 0

    def __init__(self, title, content):
        Posts.count_id += 1
        self.__posts_id = Posts.count_id
        self.__title = title
        self.__content = content
        self.__votestatus = 0
        self.__votecount = 0

    def get_posts_id(self):
        return self.__posts_id

    def get_title(self):
        return self.__title

    def get_content(self):
        return self.__content

    # def set_posts_id(self, posts_id):
    #     self.__posts_id = posts_id

    def set_title(self, title):
        self.__title = title

    def set_content(self, content):
        self.__content = content

    def get_upvote(self):  # Action of upvoting
        # If current votestatus is 0 (No Vote) or -1 (Downvote), change to 1 (Upvote)
        if self.__votestatus == -1 or self.__votestatus == 0:
            self.__votecount += 1
            self.__votestatus = 1
        else:  # Current votestatus is 1 (Upvote), change to 0 (No Vote)
            # else if votestatus = 1 (Upvote) change to 0 (No Vote)
            self.__votecount -= 1
            self.__votestatus = 0

    def get_downvote(self):  # Action of downvoting
        # If current votestatus is 0 (No Vote) or 1 (Upvote), change to -1 (Downvote)
        if self.__votestatus == 1 or self.__votestatus == 0:
            self.__votecount -= 1
            self.__votestatus = -1
        else:  # Current votestatus is 1 (Downvote), change to 0 (No Vote)
            # else if votestatus = -1 (Upvote) change to 0 (No Vote)
            self.__votecount += 1
            self.__votestatus = 0

    def get_votecount(self):
        return self.__votecount


class Comments:
    c_count_id = 0

    def __init__(self, comment, content):
        Comments.c_count_id += 1
        self.__comment_id = Comments.c_count_id
        self.__comment = comment
        self.__content = content

    def get_comment_id(self):
        return self.__comment_id

    def get_comment(self):
        return self.__comment

    def set_comment(self, comment):
        self.__comment = comment

