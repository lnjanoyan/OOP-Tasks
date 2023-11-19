import Property


class PropertyFactory:
    def create(self, type_of_property, address, features, price):
        if type_of_property == 'residential':
            return Property.ResidentalProperty(address, price, features)
        elif type_of_property == 'commercial':
            return Property.CommercialProperty(address, price, features)
