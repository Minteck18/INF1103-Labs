from discount_strategy import DiscountStrategy

class StudentDiscount(DiscountStrategy):
    def __init__(self, student_discount: float):
        self.__student_discount: float = student_discount
    
    def apply(self, total:float)->float:
        return total * 0.95