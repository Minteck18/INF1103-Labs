from product import Product 

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self,product):
        print("Add New Product")
        for existing_products in self.__products:
            if existing_products.get_product_id() == product.get_product_id():
                    return False
                        
        self.__products.append(product)
        print("Product added successfully.")
        return True

    def search_product(self, product_id):
        
        print("Search Product")
        
        for product in self.__products:
            if product.get_product_id() == product_id:
                print("Product Found")
                print("-" * 20)
                return product
                      
        return None

    def display_all_products(self):
    
        print("Current Inventory:")
        print("-"*38)
        for product in self.__products:
            print(
            f"ID: {product.get_product_id()} | Name: {product.get_product_name()} | Price: ${product.get_product_price():.2f} | Stock: {product.get_product_stock()}"
        )
        print("-"*38)

    def get_products(self):
        return self.__products.copy() 
