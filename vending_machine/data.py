class Drink:  #販賣機改寫
    def __init__(self, new_name, new_price):
        self.__name = new_name
        self.__price = new_price

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price

    def get_price(self):
        return self.__price
