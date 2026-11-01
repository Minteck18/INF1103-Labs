class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self,product):
        for existing_products in self.__products:
            if existing_products.get_product_id() == product.get_product_id():
                    return False
                        
        self.__products.append(product)
        return True

    def search_product(self, product_id):
                
        for product in self.__products:
            if product.get_product_id() == product_id:
                print("Product Found")
                print("-" * 20)
                return product
                      
        return None

    def display_all_products(self):
        print("\nCurrent Inventory")
        print("------------------------------------------")
        for product in self.__products:
            print()
            product.display_information()
        print("------------------------------------------")
        

    def get_products(self):
        return self.__products
