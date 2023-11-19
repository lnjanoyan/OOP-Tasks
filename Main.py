import System
import Factory
import Client
import Agent


def main():
    system = System.MySystem()
    factory = Factory.PropertyFactory()
    client1 = Client.Client('anna', '+6621031')
    agent1 = Agent.Agent('lily', '+654054656')
    prop1 = factory.create('commercial', 'baker street 45', 'something', 25000)
    prop2 = factory.create('residential', 'a', 'b', 5600)
    agent1.add_property(prop1)
    system.search(prop1, agent1)
    system.search(prop2, agent1)
    system.purchase(prop1, agent1, client1)
    client1.receive_info(agent1)
    print(f'Client1 history: {client1.history}')
    print('Agent1 history :', agent1.sell_history)


if __name__ == '__main__':
    main()
