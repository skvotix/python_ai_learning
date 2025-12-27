import random
from DataTypes.dataclasses import Name, Email, Phone, Message
from DataTypes.enums import MessageType, Status


class User:
    def __init__(self, name: Name, email: Email, phone_number: Phone):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number

        self.__received_messages = []


    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone_number(self):
        return self.__phone_number


    def receive_message(self, message: Message, message_type: MessageType) -> Status:
        if random.random() < 0.05:
            return Status.ERROR
        else:
            self.__received_messages.append((message, message_type))
            return Status.SUCCESS


