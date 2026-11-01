from product import Product
from canbeshipped import CanBeShipped

class PhysicalProducts(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock:int, weight: float):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f" Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
       return "Product requires physical shipping!"

    def calculate_shipping_cost(self):
        shipping_cost = self.__weight * 4
        return shipping_cost

    def to_dict(self):
        data = {"type": "physical"}
        data.update(super().to_dict())
        data["Weight"] = self.__weight
        return data
    