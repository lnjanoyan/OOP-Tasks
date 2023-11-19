import abc
import Property
import Agent
import Client


class System(abc.ABC):
    @abc.abstractmethod
    def search(self, property: Property, agent: Agent):
        pass

    @abc.abstractmethod
    def purchase(self, property: Property, agent: Agent, client: Client):
        pass


class MySystem(System):

    def search(self, property: Property, agent: Agent):
        if property in agent.available_properties:
            print('Available')
            return True
        print('Not available')
        return False

    def purchase(self, property: Property, agent: Agent, client: Client):
        if self.search(property, agent):
            client.history.append(property.address)
            agent.sell_history[f'{property.price},{property.address}'] = [client.name, client.contact_info]

