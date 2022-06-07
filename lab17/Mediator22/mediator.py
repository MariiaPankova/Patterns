from abc import ABC,abstractmethod

class Mediator(ABC):
    @abstractmethod
    def send_message_all(self, message, u_from):
        pass

    @abstractmethod
    def send_message(self, message, u_from,u_to):
        pass


class Chat(Mediator):
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.get_id()] = user

    def send_message_all(self, message, u_from):
        for k, v in self.users.items():
            if v == u_from:
                pass
            v.receive_message(message, u_from)

    def send_message(self, message, u_from, u_to):
        self.users[u_to.get_id()].receive_message(message, u_from)