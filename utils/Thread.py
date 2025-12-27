from DataTypes.objects import User, Message
from DataTypes.enums import Status, MessageType

class Thread:
    def run(self, user: User, message: Message, message_type: MessageType) -> Status:
        return user.receive_message(message, message_type)



class ReserveThread(Thread):
    def run(self, user: User, message: Message, message_type: MessageType) -> Status:
        return user.receive_message(message, message_type)
