from product import Product

class DigitalProducts(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size}MB")

    def get_fulfilment_info(self):
        return "Product delivered digitally"

    def to_dict(self):
        data = {"type": "digital"}
        data.update(super().to_dict())
        data["DownloadSize"] = self.__download_size
        return data 
    