import json
import os
from product import Product
from inventory import Inventory

INVENTORY_FILE = "inventory.json"

def load_inventory():
    inventory = Inventory()

    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")

        try:
            with open(INVENTORY_FILE, "r") as file:
                data = json.load(file)

            for item in data:
                product = Product(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )

                if not inventory.add_product(product):
                    raise ValueError("Product ID must be unique. Duplicate ID found")

            print("Inventory loaded successfully.")
            return inventory

        except (OSError, ValueError, TypeError, KeyError) as e:
            print(f"Error loading inventory.json., {e}")
            return Inventory()

    else:
        print("inventory.json not found.")
                
def save_inventory(inventory):
    
    data = []

    for product in inventory.get_products():
        product_data = {
            "product_id": product.get_product_id(),
            "name": product.get_product_name(),
            "price": product.get_product_price(),
            "stock": product.get_product_stock()
        }

        data.append(product_data)

    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    except OSError:
        print("Error saving inventory.json.")
