class Voting:
    def __init__(self):
        self.__voteCount = 0  # Encapsulated
        self.__voteStatus = 0  # 0-No Vote, 1-Upvote, -1-Downvote

    def getVoteCount(self):  # Encapsulation
        return self.__VoteCount

    def upvote(self):  # press ⬆ to upvote
        # If upvote is currrently pressed,
        # 1) Press again remove Upvote
        # 2) Press downvote it will downvote
        return self.__VoteCount

    def downvote(self):  # press ⬇ to upvote
        # If downvote is currrently pressed,
        # 1) Press again remove downvote
        # 2) Press upvote it will upvote
        self.__VoteCount -= 1
        return self.__VoteCount


vote = Voting()
vote.getVoteCount()

el