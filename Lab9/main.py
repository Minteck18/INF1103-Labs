from file_handler import load_inventory, save_inventory
from physical_products import PhysicalProducts
from digital_products import DigitalProducts
from supplier import Supplier
from validators import parse_id, parse_stock, get_valid_input, parse_weight, parse_product_type, parse_name, parse_price


def display_menu():
    print(f"{'-' * 10} MENU {'-' * 10}")
    menu = ["Display All Products", "Add Product", "Update Stock", "Search Product", "Save Inventory","Exit"]
    for i, m in enumerate(menu,start=1):
        print(f"{i}.{m}")
    print("-"*26)

def sub_menu():
    print(f"{'-' * 10} PRODUCT SUB-MENU {'-' * 10}")
    print("Add New Product")
    menu = ["Physical Product", "Digital Product"]
    for i, m in enumerate(menu, start=1):
         print(f"{i}. {m}")
    print("-"*26)

def add_product(inventory):
    print()
    sub_menu()
    option = get_valid_input("Select Product Types:",parse_product_type)
    product_id  = get_valid_input("Product ID: ", parse_id)
    product_name = get_valid_input("Product Name: ", parse_name)
    if inventory.find_product(product_id) is not None:
        print("Product ID already exists.")
        return
    price = get_valid_input("Price: ", parse_price)
    stock_quality = get_valid_input("Stock Quality: ",parse_stock)
    
    print("\nSupplier Details")
    supplier_id = get_valid_input("Supplier ID: ", parse_id)
    supplier_name = get_valid_input("Supplier Name: ", parse_name)
    supplier_email = input("Contact Email: ")
    supplier = Supplier(supplier_id, supplier_name, supplier_email)
    
    try:
        if option == "1":     
            weight = get_valid_input("Weight: ", parse_weight)
            product = PhysicalProducts(product_id, product_name, price, stock_quality,weight,supplier)

        elif option == "2":
            download_size = float(input("Download Size: "))
            product = DigitalProducts(product_id,product_name,price,stock_quality, download_size, supplier)
    
        if inventory.add_product(product):
            print("Product added successfully.")
    
    except ValueError as error:
         print(f"Invalid product type/details: {error}")

    return inventory
    
    
def search_product(inventory):
    
    print("Search Product")
    product_id = get_valid_input("Enter Product ID:", parse_id)

    product = inventory.find_product(product_id)
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
    product_id = get_valid_input("Enter Product ID: ", parse_id)

    product = inventory.find_product(product_id)
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
        user_input = input("Enter your choice:")

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