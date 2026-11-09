from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__ (self, product_id:str,name:str,price:float,stock:int, supplier:Supplier):
        self.__product_id:str = product_id
        self.__name:str = name
        self.__price:float = price 
        self.__stock:int = stock
        self.__supplier:Supplier = supplier

    def get_product_id(self)->str:
        return self.__product_id

    def get_product_name(self)->str:
        return self.__name

    def get_product_price(self)->float:
        return self.__price

    def get_product_stock(self)->int:
        return self.__stock
    
    def display_information(self)->None:
        print(f"Product ID: {self.__product_id}")
        print(f"Product Name: {self.__name}")
        print(f"Price: {self.__price}")
        print(f"Stock:  {self.__stock}")

    def to_dict(self)->dict:
        return {
            "ProductID": self.__product_id,
            "ProductName": self.__name,
            "Price": self.__price,
            "Stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }

    def display_supplier_information(self)-> None:
        self.__supplier.display_information()
    
    def update_stock(self,quantity:int)->None:
        if quantity < 0:
           return False
               
        self.__stock = quantity
        return True

    @abstractmethod
    def get_fulfilment_info(self)->str:
        pass

                




