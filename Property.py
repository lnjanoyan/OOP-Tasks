class Property:
    def __init__(self, address: str, price: float, features: str):
        self.address = address
        self.price = price
        self.features = features


class ResidentalProperty(Property):
    def get_percent(self):
        return self.price * 0.5


class CommercialProperty(Property):
    def get_percent(self):
        return self.price * 0.3
