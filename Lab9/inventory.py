from product import Product

class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self,product:Product)-> None:
        for existing_products in self.__products:
            if existing_products.get_product_id() == product.get_product_id():
                    return False
                        
        self.__products.append(product)
        return True

    def find_product(self, product_id:str)-> Product | None:
                
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
                      
        return None

    def remove_product(self,product_id:str)-> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                break
                
    def display_all_products(self)->None:
        print("\nCurrent Inventory")
        print("------------------------------------------")
        for product in self.__products:
            print()
            product.display_information()
            product.display_supplier_information()
        print("------------------------------------------")
        

    def get_products(self)->list[Product]:
        return self.__products
