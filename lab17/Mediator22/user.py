from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def send_message_all(self, message):
        pass

    @abstractmethod
    def send_message(self, message,  u_to):
        pass

    @abstractmethod
    def receive_message(self,message, u_from):
        pass


class ConcreteUser(User):
    def __init__(self, id):
        self.id = id
        self.chat = None

    def get_id(self):
        return self.id

    def set_chat(self,chat):
        self.chat = chat

    def send_message(self, message, u_to):
        self.chat.send_message(message, self, u_to)

    def receive_message(self,message, u_from):
        print(f'User{self.get_id()} receives message: {message} from user {u_from.get_id()}')

    def send_message_all(self, message):
        self.chat.send_message_all(message, self)


class ChatGroup(ConcreteUser):
    def __init__(self, id):
        super().__init__(id)
        self.group = []

    def add_user(self, user):
        self.group.append(user)

    def receive_message(self, message, u_from):
        for user in self.group:
            user.receive_message(message, u_from)
