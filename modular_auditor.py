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
    total_units  = 0
    failed_attempts = 0

    while True:
        delivery, failed = get_valid_input()
        failed_attempts += failed
        if delivery == "quit":
            break
        total_units = process_delivery(total_units,delivery)
        tax = calculate_tax(delivery)
        print("The total tax for this delivery will be:",tax)
    generate_report(total_units,failed_attempts)

main_function()