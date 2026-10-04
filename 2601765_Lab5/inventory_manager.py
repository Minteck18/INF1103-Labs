import json
import os

def display_all_products(inventory):
    print()
    print("Current Inventory:")
    print("-"*38)
    for product in inventory:
        print(f"ID: {product["ID"]} | Name: {product["Name"]} | Price: ${product["Price"]:.2f} | Stock: {product["Stock"]}")
    print("-"*38)

def add_product(inventory):
    product_id  = get_valid_input("Product ID: ", parse_product_id)
    product_name = get_valid_input("Product Name: ", parse_product_name)

    for product in inventory:
        if product["ID"] == product_id:
            print("product id must be unique") 
            return
    
    price = get_valid_input("Price: ", parse_price)
    stock_quality = get_valid_input("Stock Quality: ",parse_stock)


    new_product = {"ID": product_id, "Name": product_name, "Price": price, "Stock": stock_quality}
    inventory.append(new_product)

    print("Product added successfully.")

    return

def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found!")

    try:
        with open("inventory.json", "r") as f:
            inventory = json.load(f)

        print("Inventory loaded successfully")
    except FileNotFoundError:
        print("inventory.json not found! Starting with an empty inventory")

    return inventory

def save__inventory(inventory): 
    with open("inventory.json", "w") as f:
        json.dump(inventory,f,indent=4)
    print("Saving inventory...")
    print("Inventory successfully saved to inventory.json")

def search_product():
    pass

def update_stock(inventory):
    print("Update Stock")
    product_id = get_valid_input("Enter Product ID: ", parse_product_id)

    for product in inventory:
        if product["ID"] == product_id:
            print("Product Found:")
            print(f"Name: {product["Name"]}")
            print(f"Current Stock: {product["Stock"]}")
            new_quantity = get_valid_input("New Stock Quantity", parse_stock)
            product["Stock"] = new_quantity
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
    print("---" * 25)
    print("INVENTORY MANAGEMENT SYSTEM") 
    print("---" * 25) 
    
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

    display_menu()
    
    while True:
        user_input = get_valid_input(f"Enter your choice: ({1} - {len(selection)}):",parse_choice)
        selection[user_input](inventory)

        if selection == 6:
            break
    
main_function()

