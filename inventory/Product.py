class Product:
    def __init__(self, name, upc, stock, price):
        self.__name = name
        self.__upc = upc
        self.__stock = stock
        self.__price = price

    def get_name(self):
        return self.__name

    def get_upc(self):
        return self.__upc

    def get_stock(self):
        return self.__stock

    def get_price(self):
        return self.__price

    def set_name(self, name):
        self.__name = name

    def set_stock(self, stock):
        self.__stock = stock

    def set_price(self, price):
        self.__price = price
