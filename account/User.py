class User:

    count = 0

    def __init__(self, email, password, admin=False):
        self.__email = email
        self.__password = password
        self.__admin = admin
        self.__class__.count += 1
        self.__accountId = self.__class__.count

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def get_admin(self):
        return self.__admin

    def get_accountId(self):
        return self.__accountId

