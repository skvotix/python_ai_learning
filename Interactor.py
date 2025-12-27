from utils.Logger import Logger
from utils.Factory import Factory
from utils.Thread import Thread, ReserveThread
from DataTypes.objects import User, Message, Status
from DataTypes.enums import Attempt, MessageType

import random


class Interactor:
    def __init__(self, logger: Logger, thread: Thread, reserve_thread: ReserveThread):
        self.__logger = logger

        self.__thread = thread
        self.__reserve_thread = reserve_thread

    @staticmethod
    def create_object(factory: Factory, *args, **kwargs):
        return factory.create(*args, **kwargs)

    def run_thread(self, user: User, message: Message, message_type: MessageType) -> Status:
        attempt_status = self.__thread.run(user, message, message_type)

        self.__logger.log(Attempt.DEFAULT)

        if attempt_status == Status.SUCCESS:
            self.__logger.log(Attempt.SUCCEED)
            return Status.SUCCESS

        return Status.ERROR


    def run_reserve_thread(self, user: User, message: Message, message_type: MessageType) -> Status:
        reserve_attempt = self.__reserve_thread.run(user, message, message_type)

        if reserve_attempt == Status.SUCCESS:
            self.__logger.log(Attempt.FIXED)
            return Status.SUCCESS

        self.__logger.log(Attempt.ERROR)
        return Status.ERROR


    def get_statistics(self) -> dict:
        return self.__logger.send_logs()








