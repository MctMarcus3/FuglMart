class Product:
    def __init__(self, name, upc, stock, category, company, price):
        self.__name = name
        self.__upc = upc
        self.__stock = stock
        self.__category = category
        self.__company = company
        self.__price = price

    def get_name(self):
        return self.__name

    def get_upc(self):
        return self.__upc

    def get_stock(self):
        return self.__stock

    def get_company(self):
        return self.__company

    def get_price(self):
        return self.__price

    def get_category(self):
        return self.__category

    def set_name(self, name):
        self.__name = name

    def set_stock(self, stock):
        self.__stock = stock

    def set_price(self, price):
        self.__price = price

    def set_company(self, company):
        self.__company = company

    def set_category(self, category):
        self.__category = category
