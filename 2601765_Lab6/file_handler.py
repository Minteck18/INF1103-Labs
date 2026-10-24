import json

from product import Product
from inventory import Inventory

INVENTORY_FILE = "inventory.json"

def load_inventory(file=INVENTORY_FILE):
    inventory = Inventory()
    try:
        with open(file, "r") as f:
            inventory = json.load(f)

        for item in inventory:
            product = Product(item['product_id'], item['name'],item['price'], item['stock']) 

            if not inventory.add_product(product):
                raise ValueError("Product ID must be unique. Duplicate ID found")
                    
        print("inventory.json found!")
        print("Inventory loaded successfully")
        return inventory
        
    except FileNotFoundError:
        print("inventory.json not found! Starting with an empty inventory")

    

def save__inventory(inventory): 
    data = []

    for product in inventory.get_products():
        product_details = {
            "product_id": product.get_product_id(),
            "product_name": product.get_product_price(),
            "product_price": product.get_product_price(),
            "product_stock": product.get_product_stock()
        }
    
        data.append(product_details)
    
    with open("inventory.json", "w") as f:
        json.dump(inventory,f,indent=4)
    
    print("Saving inventory...")
    print("Inventory successfully saved to inventory.json")
