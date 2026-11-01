from validators import get_valid_input, parse_product_id, parse_product_name, parse_price, parse_stock


class ProductInputHandler:
    
    def get_product_id():
        product_id = get_valid_input("Product ID: ", parse_product_id)
        return product_id

    def get_product_name():
        product_name = get_valid_input("Product Name: ", parse_product_name)
        return product_name

    def get_product_price():
        price = get_valid_input("Price: ", parse_price)
        return price

    def get_product_stock():        
        stock_quality = get_valid_input("Stock Quality: ",parse_stock)
        return stock_quality