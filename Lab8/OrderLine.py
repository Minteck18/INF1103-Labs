from product import Product

class OrderLine:
    def __init__(self, products: Product, quantity: int):
        self.__product: Product = products
        self.__quantity: int = quantity
        
    def calculate_subtotal(self)->float:
        return self.__product.get_product_price() * self.__quantity 
        