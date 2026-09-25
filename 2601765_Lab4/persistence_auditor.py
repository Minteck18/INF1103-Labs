def get_valid_input():
    failed_attempts = 0
    while True:
        product_name = input("Enter product name or type quit to exit").strip()
        if product_name.lower() == "quit":
            return None, None, failed_attempts
    
        inventory = input("Enter Quantity or type quit exit").strip()
        if inventory.lower() == "quit":
            return None, None, failed_attempts
        if not inventory.isdigit():
           failed_attempts += 1
           print("Invalid input! Please enter a valid integer")
           continue
        return product_name,int(inventory), failed_attempts

def process_delivery(current_total, new_value):    
     new_total = current_total + new_value
     return new_total

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units,failed_attempts):
    print("\n"+ "="*4 + "Audit Report" + "="*4)
    print("Total Transactions Processed:",total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    
def main_function():
    total_units,transaction_history = load_inventory()
    failed_attempts = 0
    while True:
        product,delivery, failed = get_valid_input()
        failed_attempts += failed
        if product is None:
            save_inventory(total_units,transaction_history)
            break
        order_id = 1001 if not transaction_history else max(order[0] for order in transaction_history)+1
        total_units = process_delivery(total_units,delivery)
        new_orders = (order_id,product,delivery)
        transaction_history.append(new_orders)
        tax = calculate_tax(delivery)
        total_inventory = sum(order[2] for order in transaction_history if order[1]==product)
        print("\n"+ "New Order added:")
        print(f"{new_orders[0]},{new_orders[1]},{new_orders[2]}")
        print(f"Tax: ${tax:.2f} | Inventory for {product}: {total_inventory}\n")
        save_inventory(total_units, transaction_history)
    generate_report(total_units,failed_attempts)

def load_inventory():
     
    total_units = 0
    transaction_history = []
    
    try:
        with open('inventory.txt', 'r') as file:
            orders = file.readlines()
            if orders:
                 total_units = int(orders[0].strip())
                 for order in orders[1:]:
                      if ":" in order:
                        product_details = order.split(":")
                        order_id = int(product_details[0].strip())
                        product_name = product_details[1].strip()
                        quantity = int(product_details[2].strip())
                        transaction_history.append((order_id,product_name, int(quantity)))
            print("Inventory record loaded")
            print("Current Orders:")
            print("-"*20)
            for order_id,product_name,quantity in transaction_history:
               print(f"{order_id}, {product_name}, {quantity}")
            print("-"*20)
    except FileNotFoundError as err:
         print("No previous order found!")
    return total_units, transaction_history

def save_inventory(total_units,transaction_history):
        with open('inventory.txt', "w") as file:
          file.write(str(total_units)+"\n")
          for order_id, product, quantity in transaction_history:
            file.write(f"{order_id}:{product}:{quantity}\n")
          print("Order successfully saved to inventory.txt")
        
main_function()