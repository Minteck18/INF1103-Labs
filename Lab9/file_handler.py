import csv
import json
from product_factory import ProductFactory
from inventory import Inventory
from physical_products import PhysicalProducts
from digital_products import DigitalProducts
from supplier import Supplier
import os 

PRODUCT_FILE = "products.csv"
rows = []

INVENTORY_FILE = "inventory.json"

def load_inventory():
    inventory = Inventory()

    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")

        try:
            with open(INVENTORY_FILE, "r") as file:
                data = json.load(file)

            for item in data:
                if "supplier" in item:
                    supplier_data = item["supplier"]
                    supplier = Supplier(
                    supplier_data["SupplierID"],
                    supplier_data["SupplierName"],
                    supplier_data["ContactEmail"]
                )

            
                if item["type"] == "physical":
                    product = PhysicalProducts(
                    item["ProductID"],
                    item["ProductName"],
                    item["Price"],
                    item["Stock"],
                    item["Weight"],
                    supplier

                )
                elif item["type"] == "digital":
                    product = DigitalProducts(
                        item["ProductID"],
                        item["ProductName"],
                        item["Price"],
                        item["Stock"],
                        item["DownloadSize"],
                        supplier
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

def load_products(path: str, inventory: Inventory, supplier:Supplier)->None:
        loaded = 0
    
        try:
            with open(path, newline= "", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                next(csv_reader, None)
                for row_number, row in enumerate(csv_reader, start=2):
                    try:
                        product_type,product_id,name,price,stock_quantity = row
                        product = ProductFactory.create(product_type, product_id, name, float(price), int(stock_quantity),supplier)
                        inventory.add_product(product)
                        loaded += 1
                    except ValueError as error:
                        raise ValueError(f"Invalid data on {row_number}: {error}")
        except FileNotFoundError:
                    raise FileNotFoundError(f"Product does not exists on {path}")
        finally:
            print(f"{loaded} products loaded")
            print("Load attempt finished.")
        return loaded
                     
                     

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