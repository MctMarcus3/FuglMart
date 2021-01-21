class Item:
    item_count = 0
    def __init__(self, item_name, item_amount, item_price, item_code):
        item.item_count += 1
        self.__item_name = item_name
        self.__item_amount = item_amount
        self.__receit_number = item.item_count
        self.__item_price = item_price
        self.__item_code = item_code

    def get_item_code(self):
        return self.__item_code

    def get_item_name(self):
        return self.__item_name

    def get_item_amount(self):
        return self.__item_amount

    def get_receit_number(self):
        return self.__receit_number

    def get_item_price(self):
        return self.__item_price

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def set_item_amount(self, item_amount):
        self.__item_amount = item_amount

    def set_receit_number(self, receit_number):
        self.__receit_number = receit_number

    def set_item_price(self, item_price):
        self.__item_price = item_price
