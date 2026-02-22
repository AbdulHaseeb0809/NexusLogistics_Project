from abc import ABC, abstractmethod
class Base_Delivery(ABC):
    def __init__(self, item_name, weight):
        self.item_name = item_name
        self.weight = weight
        self.__tracking_id = "NEXUS-123"
        super().__init__()
    @abstractmethod
    def calculate_shipping(self):
        pass
    @property
    def tracking_id(self):
        print("Fetching Tracking id Safely...")
        return self.__tracking_id