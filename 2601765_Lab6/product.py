class Product:
    def __init__ (self, product_id,name,price,stock):
        self._product_id = product_id
        self._name = name
        self._price = price 
        self._stock = stock


    def get_product_id(self):
        return self._product_id

    def get_product_name(self):
        return self._name

    def get_product_price(self):
        return self._price

    def get_product_stock(self):
        return self._stock
 
    def update_stock(self,quantity):
        if quantity < 0:
           return False
               
        self._stock = quantity
        return True
            
    print("Stock Updated Successfully!")





