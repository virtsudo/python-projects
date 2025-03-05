from Bank.Bank import Bank
from Bank.GUI.GUI import *
from datetime import datetime


class Main:
    def __init__(self):
        self.mode = False

    def main(self):
        self.mode = True
        bank = Bank("Unicredit")
        bank.create_account("Willy", datetime.now(), 100.0)
        gui = GUI(bank)


if __name__ == '__main__':
    Main.main(Main())
