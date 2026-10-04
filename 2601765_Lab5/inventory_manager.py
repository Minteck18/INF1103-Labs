def display_all_products(inventory):
    print()
    print("Current Inventory:")
    print("-"*38)
    for product in inventory:
        print(f"ID: {product["ID"]} | Name: {product["Name"]} | Price: ${product["Price"]:.2f} | Stock: {product["Stock"]}")
    print("-"*38)


def display_menu():
    print(f"{'-' * 10} MENU {'-' * 10}")
    menu = ["Display All Products", "Add Product", "Update Stock", "Search Product", "Save Inventory", "Exit"]
    for i, m in enumerate(menu,start=1):
        print(f"{i}.{m}")
    print("-"*26)
    

def main_function():
    print("---" * 25)
    print("INVENTORY MANAGEMENT SYSTEM") 
    print("---" * 25) 
    
    inventory = [
        {"ID": "P001", "Name": "Laptop", "Price": 1200, "Stock": 15},
        {"ID": "P002", "Name": "Mouse", "Price": 25.50, "Stock": 40},
        {"ID": "P003", "Name": "Keyboard", "Price": 45, "Stock": 25}
    ]

    selection = {
        1: display_all_products
    }

    display_menu()
    
    while True:
        user_input = int(input(f"Enter your choice:"))
        selection[user_input](inventory)
        
    
main_function()

