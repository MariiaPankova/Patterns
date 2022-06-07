from mediator import Chat
from user import ConcreteUser, ChatGroup

if __name__ == '__main__':
    user1 = ConcreteUser('u1')
    user2 = ConcreteUser('u2')
    user3 = ConcreteUser('u3')
    user4 = ConcreteUser('u4')
    user5 = ConcreteUser('u3')
    user6 = ConcreteUser('u4')

    group = ChatGroup("group1")
    group.add_user(user5)
    group.add_user(user6)

    chat = Chat()
    chat.add_user(user1)
    chat.add_user(user2)
    chat.add_user(user3)
    chat.add_user(user4)
    chat.add_user(group)


    user1.set_chat(chat)
    user2.set_chat(chat)
    user3.set_chat(chat)
    user4.set_chat(chat)

    chat.send_message_all("hello, world!", user2)
    user2.send_message('Hi there!', user3)
    chat.send_message("Hi group", user1, group)