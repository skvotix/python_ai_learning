from Interactor import Interactor
from UserDialog import Dialog
from DataValidators import *
from utils.Factory import UserFactory, MessageFactory
from DataTypes.enums import MessageType, Status
from DataTypes.objects import User, Message
from constants import *
import random

from datetime import datetime

class Scenario:
    def __init__(self, interactor: Interactor, dialog: Dialog):
        self.__interactor = interactor
        self.__dialog = dialog

    def start(self):
        message_type = MessageType

        string_validator = TypeValidator(_type = str)
        raw_message = self.__dialog.ask_data("Write your message:", string_validator)

        int_validator = TypeValidator(_type = int)
        amount_of_users = self.__dialog.ask_data("The amount of receivers:", int_validator)
        amount_of_users = int(amount_of_users)

        print("\n")

        users = []
        users_factory = UserFactory()
        for user_index in range(1, amount_of_users + 1):
            self.__dialog.write(f"Receiver №{user_index}:")
            name = self.__dialog.ask_data("\tName:", NameValidator())
            email = self.__dialog.ask_data("\tEmail:", EmailValidator())
            phone = self.__dialog.ask_data("\tPhone number:", PhoneNumberValidator())

            message_type_raw = self.__dialog.ask_data("Message type (Email/SMS/Push):", MessageTypeValidator())
            message_type = MessageType(message_type_raw.lower().strip())

            user = self.__interactor.create_object(users_factory, name, email, phone)

            users.append((user, message_type))

            self.__dialog.write("\n" )

        self.__dialog.write("\n" * 2)

        self.__dialog.write(f"Message sending started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.__dialog.write("\n")


        for attempt_index in range(amount_of_users):
            current_user = users[attempt_index]

            self.__dialog.write(f"Attempt №{attempt_index + 1}")
            self.__dialog.write(f"\tReceiver: {current_user[0].name.value}")
            self.__dialog.write(f"\tMessage type: {current_user[1].value}")

            message_factory = MessageFactory()
            at_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = self.__interactor.create_object(message_factory, raw_message, at_time)

            attempt_status = self.__interactor.run_thread(current_user[0], message, current_user[1])
            if attempt_status == Status.SUCCESS:
                self.__dialog.write("\tStatus: Succeed")
                self.__dialog.write(f"\tTime: {at_time}")
                self.__dialog.write("\n")
                continue

            self.__dialog.write("\tStatus: Error (could not send)")
            self.__dialog.write(f"\tTime: {at_time}")

            reserve_message_types = list(MESSAGE_TYPES)
            reserve_message_types.remove(message_type.value)
            reserve_message_type_raw: str = random.choice(reserve_message_types)
            reserve_message_type = MessageType(reserve_message_type_raw)

            self.__dialog.write(f"\tReserve thread: {reserve_message_type_raw.capitalize()}")
            reserve_attempt_status = self.__interactor.run_reserve_thread(current_user[0], message, reserve_message_type)

            if reserve_attempt_status == Status.SUCCESS:
                self.__dialog.write("\tReserve thread status: Succeed")
            else:
                self.__dialog.write("\tReserve thread status: Error")

            self.__dialog.write("\n")

        self.__dialog.write("All messages sent!")
        self.__dialog.write("Summary:")

        statistics = self.__interactor.get_statistics()

        self.__dialog.write(f"\tAttempts: {statistics[JSON_ATTEMPTS_KEY]}")
        self.__dialog.write(f"\tSucceed: {statistics[JSON_SUCCEED_ATTEMPTS_KEY]}")
        self.__dialog.write(f"\tErrors: {statistics[JSON_ERROR_ATTEMPTS_KEY]}")
        self.__dialog.write(f"\tErrors fixed: {statistics[JSON_FIXED_ERROR_ATTEMPTS_KEY]}")






















