import json
import os

INVENTORY_FILE = "inventory.json"

def display_all_products(inventory):
    print()
    print("Current Inventory:")
    print("-"*38)
    for product in inventory:
        print(
            f"ID: {product['ID']} | Name: {product['Name']} | Price: ${product['Price']:.2f} | Stock: {product['Stock']}"
        )
    print("-"*38)

def add_product(inventory):
    print()
    print("Add New Product")
    product_id  = get_valid_input("Product ID: ", parse_product_id)
    product_name = get_valid_input("Product Name: ", parse_product_name)

    for product in inventory:
        if product['ID'] == product_id:
            print("product id must be unique") 
            return
    
    price = get_valid_input("Price: ", parse_price)
    stock_quality = get_valid_input("Stock Quality: ",parse_stock)


    new_product = {"ID": product_id, "Name": product_name, "Price": price, "Stock": stock_quality}
    inventory.append(new_product)

    print()
    print("Product added successfully.")
    print()

    return

def load_inventory(file=INVENTORY_FILE):
    
    try:
        with open(file, "r") as f:
            inventory = json.load(f)
        print("inventory.json found!")
        print("Inventory loaded successfully")
        print()

        return inventory
    
    except FileNotFoundError:
        print("inventory.json not found! Starting with an empty inventory")

    

def save__inventory(inventory): 
    with open("inventory.json", "w") as f:
        json.dump(inventory,f,indent=4)
    print()
    print("Saving inventory...")
    print("Inventory successfully saved to inventory.json")
    print()

def search_product(inventory):
    print()
    print("Search Product")
    product_id = get_valid_input("Enter Product ID:", parse_product_id)

    is_found = False

    print()
    for product in inventory:
        if product['ID'] == product_id:
            print("Product Found")
            print("-" * 20)
            print(f"ID: {product['ID']}")
            print(f"Name: {product['Name']}")
            print(f"Price: {product['Price']}")
            print(f"Stock:  {product['Stock']}")
            print("-" * 20)
            print()
            is_found = True
            break 

    if not is_found:
        print("Product not found")  

def update_stock(inventory):
    print()
    print("Update Stock")
    product_id = get_valid_input("Enter Product ID: ", parse_product_id)

    is_found = None
    
    print()
    for product in inventory:
        if product['ID'] == product_id:
            is_found = product
            break
    if is_found is None:
            print("product not found")
            return

    print("Product Found:")
    print(f"Name: {is_found['Name']}")
    print(f"Current Stock: {is_found['Stock']}")
    print()

    new_quantity = get_valid_input("New Stock Quantity: ", parse_stock)
    is_found["Stock"] = new_quantity
    print()

    print("Stock Updated Successfully!")
                
def display_menu():
    print(f"{'-' * 10} MENU {'-' * 10}")
    menu = ["Display All Products", "Add Product", "Update Stock", "Search Product", "Save Inventory", "Exit"]
    for i, m in enumerate(menu,start=1):
        print(f"{i}.{m}")
    print("-"*26)

def parse_product_id(user_input):
    if not user_input:
        raise ValueError("Product ID cannot be empty")
    return user_input

def parse_product_name(user_input):
    if not user_input:
        raise ValueError("Product Name cannot be empty")
    return user_input

def parse_price(user_input):
    if not user_input.isdigit():
        raise ValueError("Price must be a whole number")
    return int(user_input)

def parse_stock(user_input):
    if not user_input.isdigit():
        raise ValueError("Stock must be a whole number")
    return int(user_input)

def get_valid_input(prompt,parse):
    while True:
        user_input = input(prompt).strip()
        try:
            return parse(user_input)
        except ValueError as e:
            print(e)

def parse_choice(user_input):
    if not user_input.isdigit() or not 1 <= int(user_input) <= 6:
        raise ValueError("Please enter a valid choice") 
    return int(user_input)

def exit_from_program(inventory):
    print("Saving inventory before exit...")
    with open("inventory.json", "w") as f:
            json.dump(inventory,f,indent=4)

    print("Inventory saved successfully.")
    print("Thank you for using Inventory Management System")
    print("Program terminated")

def main_function():
    print("---" * 12)
    print("INVENTORY MANAGEMENT SYSTEM") 
    print("---" * 12) 
    print()
    
    inventory = load_inventory()

    selection = {
        1: display_all_products,
        2: add_product,
        3: update_stock,
        4: search_product,
        5: save__inventory,
        6: exit_from_program
    }

    ''' part a)
    inventory = [
        {"ID": "P001", "Name": "Laptop", "Price": 1200, "Stock": 15},
        {"ID": "P002", "Name": "Mouse", "Price": 25.50, "Stock": 40},
        {"ID": "P003", "Name": "Keyboard", "Price": 45, "Stock": 25}
    ]
    '''

    print()
    display_menu()
    
    while True:
        user_input = get_valid_input(f"Enter your choice: ({1} - {len(selection)}):",parse_choice)
        selection[user_input](inventory)

        if selection == 6:
            break
    
main_function()

