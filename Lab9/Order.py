from OrderLine import OrderLine
from product import Product
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount

class Order:
    def __init__(self, order_id: str, discount_strategy: DiscountStrategy|None = None):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = (discount_strategy if discount_strategy is not None else NoDiscount())

   

    def add_order_line(self, product: Product, quantity: int) -> None:
        if quantity < 0:
            raise ValueError(f"Invalid Quantity.")

        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self)-> float:
        total = sum(line.calculate_subtotal() for line in self.__order_lines)
        return self.__discount.apply(total)

    def set_discount(self, discount_strategy: DiscountStrategy | None = None):
        self.__discount = discount_strategy