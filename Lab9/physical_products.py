from product import Product
from canbeshipped import CanBeShipped
from supplier import Supplier

class PhysicalProducts(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock:int, weight: float, supplier:Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def display_information(self)->None:
        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self)->str:
       return "Product requires physical shipping!"

    def calculate_shipping_cost(self)->float:
        shipping_cost = self.__weight * 4
        return shipping_cost

    def to_dict(self)->dict:
        data = {"type": "physical"}
        data.update(super().to_dict())
        data["Weight"] = self.__weight
        return data
    