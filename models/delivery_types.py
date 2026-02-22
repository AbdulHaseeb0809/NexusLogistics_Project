from .base import Base_Delivery
class Express_Delivery(Base_Delivery):
    def __init__(self, item_name, weight,):
        super().__init__(item_name,weight)
    def calculate_shipping(self):
        return self.weight*150
class Standard_Delivery(Base_Delivery):
    def __init__(self, item_name, weight):
        super().__init__(item_name, weight)
    def calculate_shipping(self):
        return self.weight*50