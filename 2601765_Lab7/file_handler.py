import json
import os
from physical_products import PhysicalProducts
from digital_products import DigitalProducts
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
                if item["type"] == "physical":
                    product = PhysicalProducts(
                    item["ProductID"],
                    item["ProductName"],
                    item["Price"],
                    item["Stock"],
                    item["Weight"]
                )
                elif item["type"] == "digital":
                    product = DigitalProducts(
                        item["ProductID"],
                        item["ProductName"],
                        item["Price"],
                        item["Stock"],
                        item["DownloadSize"]
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
    products = inventory.get_products()
    for product in products:
        data.append(product.to_dict())

    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    except OSError:
        print("Error saving inventory.json.")
