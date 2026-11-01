def parse_product_id(user_input):
    if not user_input:
        raise ValueError("Product ID cannot be empty")
    return user_input

def parse_product_name(user_input):
    if not user_input:
        raise ValueError("Product Name cannot be empty")
    return user_input

def parse_product_type(user_input):
    if not user_input:
        raise ValueError("Product Type cannot be empty")
    if not "1" <= user_input <= "2":
        raise ValueError("Product Type must be 1 or 2")
    return user_input

def parse_price(user_input):
    try:
        price = float(user_input)
    except ValueError:
        raise ValueError("Price must be a number")
    
    if price <= 0:
        raise ValueError("Price must not be less than 0")
    
    return price

def parse_weight(user_input):
    try:
        weight = float(user_input)
    except ValueError:
        raise ValueError("Weight must be a number")
    
    if weight <= 0:
        raise ValueError("Weight must not be negative")
    
    return weight

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

