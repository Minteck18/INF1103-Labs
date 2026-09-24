def get_valid_input():
    inventory = 0;
    failed_attempts = 0
    while True:
        inventory = input("Please enter the stock quantity or type quit to exit")
        if inventory.lower() == "quit":
                return "quit", failed_attempts
        if not inventory.isdigit():
                failed_attempts += 1
                print("Invalid input! Please enter a valid integer")
                continue
        return int(inventory), failed_attempts

def process_delivery(current_total, new_value):    
     new_total = current_total + new_value
     return new_total

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units,failed_attempts):
    print("This Is The Total Deliveries Processed:",total_units)
    print("Number Of Failed/Rejected Entries:",failed_attempts)

def main_function():
    total_units,transaction_history = load_inventory()
    failed_attempts = 0
    while True:
        delivery, failed = get_valid_input()
        failed_attempts += failed
        if delivery == "quit":
            save_inventory(total_units,transaction_history)
            break
        total_units = process_delivery(total_units,delivery)
        transaction_history.append(str(delivery))
        print("New Transaction added: " + "\n" + str(delivery))
        tax = calculate_tax(delivery)
        print("The total tax for this delivery will be:",tax)
    generate_report(total_units,failed_attempts)

def load_inventory():
    total_units = 0
    transaction_history = []

    try:
        with open('inventory.txt', 'r') as file:
            orders = file.readlines()
            if orders:
                 total_units = int(orders[0].strip())
                 transaction_history = [int(i.strip()) for i in orders[1] if i.strip().isdigit()]
            print("inventory record loaded")
            print("Current total:"+ "\n")
            print(total_units)
            print("transaction history:")
            for i in transaction_history:
                print(i)
            
    except FileNotFoundError as err:
         print("No inventory is found!")
    return total_units, transaction_history

def save_inventory(total_units,transaction_history):
        with open('inventory.txt', "w") as file:
          file.write(str(total_units)+"\n")
          for i in transaction_history:
            file.write(str(i))
        print("Transaction successfully saved to inventory.txt")
        
main_function()