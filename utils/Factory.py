from abc import ABC, abstractmethod
from DataTypes.dataclasses import Phone, Email, Name, Message
from DataTypes.objects import User
from DataTypes.enums import MessageType



class Factory(ABC):
    @staticmethod
    @abstractmethod
    def create(*args, **kwargs) -> object:
        pass


class UserFactory(Factory):
    @staticmethod
    def create(name: str, email: str, phone_number: str) -> User:

        return User (
            Name(name),
            Email(email),
            Phone(phone_number)
        )


class MessageFactory(Factory):
    @staticmethod
    def create(text: str, at_time: str) -> Message:
         return Message(text, at_time)


class MessageTypeFactory(Factory):
    @staticmethod
    def create(message_type_text: str) -> MessageType:
        pass