from abc import ABC, abstractmethod

class Product(ABC):
    def __init__ (self, product_id:int,name:str,price:float,stock:int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price 
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__name

    def get_product_price(self):
        return self.__price

    def get_product_stock(self):
        return self.__stock
    
    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Product Name: {self.__name}")
        print(f"Price: {self.__price}")
        print(f"Stock:  {self.__stock}")

    def to_dict(self):
        return {
            "ProductID": self.__product_id,
            "ProductName": self.__name,
            "Price": self.__price,
            "Stock": self.__stock
        }
    
    def update_stock(self,quantity):
        if quantity < 0:
           return False
               
        self.__stock = quantity
        return True

    @abstractmethod
    def get_fulfilment_info(self):
        pass

                




