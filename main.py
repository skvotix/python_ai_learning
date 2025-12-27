from Scenario import Scenario
from UserDialog import Dialog
from Interactor import Interactor
from utils.Logger import Logger
from constants import *
from utils.Thread import Thread, ReserveThread

def main():
    logger = Logger(JSON_FILENAME)
    logger.setup()

    thread = Thread()
    reserve_thread = ReserveThread()

    interactor = Interactor(logger, thread, reserve_thread)
    dialog = Dialog()


    scenario = Scenario(interactor, dialog)

    scenario.start()


def test():
    import random
    flag = True
    if random.random() < 0.05:
        flag = False
    print(flag)

    if random.random() < 0.05:
        flag = False
    print(flag)

if __name__ == "__main__":
    main()



