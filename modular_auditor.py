inventory = 0; 
total = 0

def get_valid_input():
    failed_attempts = 0
    while True:
        stock_quantity = input("Please enter the stock quantity or type quit to exit")
        stock_quantity = int(stock_quantity)
        if stock_quantity > 0:
               total += int(stock_quantity) 
               print("current running total", total)
        if stock_quantity < 0: 
            failed_attempts += 1
            print("Negative numbers are not allowed!")
        if total > 500:
            print("The inventory has exceed 500 units!")
            break
        if stock_quantity == "quit":
           return "quit", failed_attempts
        if stock_quantity != stock_quantity.isdigit():
            failed_attempts += 1
            print("Invalid input! Please enter a integer")
        
    return int(stock_quantity), failed_attempts

def process_delivery(current_total, new_value):    
     return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units,failed_attempts):
    print(f"Total Units Processed:",total_units)
    print(f"Number of failed/rejected entries",failed_attempts)
