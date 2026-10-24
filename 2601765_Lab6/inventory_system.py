import json
from file_handler import load_inventory, save_inventory
from product import Product
from inventory import Inventory
from validators import parse_price, parse_product_id, parse_product_name, parse_stock, get_valid_input

def exit_from_program(inventory):
    print("Saving inventory before exit...")
    save_inventory(inventory)

    print("Inventory saved successfully.")
    print("Thank you for using Inventory Management System")
    print("Program Terminated")


def display_menu():
    print(f"{'-' * 10} MENU {'-' * 10}")
    menu = ["Display All Products", "Add Product", "Update Stock", "Search Product", "Save Inventory", "Exit"]
    for i, m in enumerate(menu,start=1):
        print(f"{i}.{m}")
    print("-"*26)

def add_product(inventory):
    print()
    print("Add New Product")
    product_id  = get_valid_input("Product ID: ", parse_product_id)
    product_name = get_valid_input("Product Name: ", parse_product_name)

    
    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return
    
    price = get_valid_input("Price: ", parse_price)
    stock_quality = get_valid_input("Stock Quality: ",parse_stock)

    product = Product(product_id, product_name, price, stock_quality)
    
    inventory.add_product(product)
    print("Product added successfully.")

    return inventory

def search_product(inventory):
    
    print("Search Product")
    product_id = get_valid_input("Enter Product ID:", parse_product_id)

    product = inventory.search_product(product_id)
    if product is None:
            print("Product not found")  
            return

    
    print("Product Found")
    print("-" * 20)
    print(f"ID: {product.get_product_id()}")
    print(f"Name: {product.get_product_name()}")
    print(f"Price: {product.get_product_price()}")
    print(f"Stock:  {product.get_product_stock()}")
    print("-" * 20)
    print()

def update_stock(inventory):
    print()
    print("Update Stock")
    product_id = get_valid_input("Enter Product ID: ", parse_product_id)

    product = inventory.search_product(product_id)
    if product is None:
                print("Product not found")  
                return

    print("Product Found:")
    print(f"Name: {product.get_product_name()}")
    print(f"Current Stock: {product.get_product_stock()}")
    print()

    new_quantity = get_valid_input("New Stock Quantity: ", parse_stock)
    if product.update_stock(new_quantity):
         print("Stock Updated Successfully!")
    else:
         print("Stock cannot be negative")
    print()


def exit_from_program(inventory):
    print("Saving inventory before exit...")
    save_inventory(inventory)

    print("Thank you for using Inventory Management System")
    print("Program Terminated")

def main_function():
    print("---" * 12)
    print("INVENTORY MANAGEMENT SYSTEM") 
    print("---" * 12) 
    inventory = load_inventory()

    
    while True:     
        display_menu()
        user_input = input(f"Enter your choice:")

        if user_input == "1":
            inventory.display_all_products()

        elif user_input == "2":
            add_product(inventory)

        elif user_input == "3":
            update_stock(inventory)

        elif user_input == "4":
            search_product(inventory)

        elif user_input == "5":
            save_inventory(inventory)

        elif user_input == "6":
            exit_from_program(inventory)
            break

        else:
             print("Invalid option, please enter a option from 1-6!")


main_function()