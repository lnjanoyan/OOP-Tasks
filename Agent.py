import Property

class Agent:

    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.available_properties = []
        self.sell_history = {}

    def add_property(self, property: Property):
        self.available_properties.append(property)

    def delete_property(self, property: Property):
        if property in self.available_properties:
            del property
            print('Successfully deleted')
        else:
            print('No such property in list')
