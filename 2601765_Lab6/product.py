class Product:
    def __init__ (self, product_id,name,price,stock):
        self._product_id = product_id
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
 
    def update_stock(self,quantity):
        if quantity < 0:
           return False
               
        self.__stock = quantity
        return True
            
    print("Stock Updated Successfully!")





