from discount_strategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold:int, amount:int):
        self.__threshold:int = threshold
        self.__amount:int = amount

    def apply(self, total:float)->float:
        if total >= self.__threshold:
            return max(0.0, total - self.__amount)
        return total

    