import csv
from product_factory import ProductFactory
from inventory import Inventory
from supplier import Supplier

PRODUCT_FILE = "products.csv"
rows = []

def load_products(path: str, inventory: Inventory, supplier:Supplier)->None:
    
        try:
            file = open(path, newline= "")
        except FileNotFoundError:
            raise FileNotFoundError(f"Product does not exists on {path}")
        else:
            with file:
                 csv_reader = csv.reader(file)
                 next(csv_reader, None)
                 row_number = 1
                 for row in csv_reader:
                    try:
                        product_type,product_id,name,price,stock_quantity = row
                        product = ProductFactory.create(product_type, product_id, name, float(price), int(stock_quantity),supplier)
                        inventory.add_product(product)
                        loaded += 1
                    except ValueError as error:
                     raise ValueError(f"Invalid input on {rows}")
            print(f"{loaded} products loaded")
        finally:
            print("Load attempt finished.")
                     
                     

def save_inventory(inventory):
    
    data = []
    products = inventory.get_products()
    for product in products:
        data.append(product.to_dict())

    try:
        with open(PRODUCT_FILE, "w") as file:

            print("Product saved successfully to products.csv.")

    except OSError:
        print("Error saving products.csv.")
