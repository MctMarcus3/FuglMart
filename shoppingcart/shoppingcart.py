class Item:
    item_count = 0
    def __init__(self, item_name, item_amount, item_price, item_code, item_count=0,):
        Item.item_count += 1
        self.__item_no = Item.item_count
        self.__item_name = item_name
        self.__item_amount = item_amount
        self.__receipt_number = item_count
        self.__item_price = item_price
        self.__item_code = item_code

    def get_item_code(self):
        return self.__item_code

    def get_item_name(self):
        return self.__item_name

    def get_item_amount(self):
        return self.__item_amount

    def get_receipt_number(self):
        return self.__receipt_number

    def get_item_price(self):
        return self.__item_price

    def set_item_code(self, item_code):
        self.__item_code = item_code

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def set_item_amount(self, item_amount):
        self.__item_amount = item_amount

    def set_receipt_number(self, receipt_number):
        self.__receipt_number = receipt_number

    def set_item_price(self, item_price):
        self.__item_price = item_price
