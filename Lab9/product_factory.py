from physical_products import PhysicalProducts
from digital_products import DigitalProducts
from product import Product
from supplier import Supplier

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
        stock_quantity: int, supplier: Supplier, weight:float|None = None, download_size:int|None = None) -> Product:
        if product_type == "physical":
            if weight is None:
                raise ValueError(
                    "Weight is required for physical products."
                )
            return PhysicalProducts(product_id, name, price, stock_quantity,weight, supplier)
        elif product_type == "digital":
            if download_size is None:
                raise ValueError(
                    "Download size is required for digital products."
                )
            return DigitalProducts(product_id, name, price, stock_quantity,download_size, supplier)
        else:
         raise ValueError(f"Unknown product type: {product_type}")