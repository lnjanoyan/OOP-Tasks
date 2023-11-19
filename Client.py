import Agent


class Client:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.history = []

    def receive_info(self, agent: Agent):
        print(f'Agent info: {agent.name},{agent.contact_info}')