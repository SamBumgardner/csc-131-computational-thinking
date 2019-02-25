"""
File: atm.py

This module defines the ATM class and its application.

To test, launch from Idle and run

>>> createBank(5)
>>> main()

"""

from bank import Bank, SavingsAccount

class ATM(object):
    """This class represents terminal-based ATM transactions."""
        
    SECRET_CODE = "CloseItDown"

    def __init__(self, bank):
        self._account = None
        self._bank = bank
        self._methods = {}          # Jump table for commands
        self._methods["1"] = self._getBalance
        self._methods["2"] = self._deposit
        self._methods["3"] = self._withdraw
        self._methods["4"] = self._quit

    def run(self):
        """Logs in users and processes their accounts."""
        while True:
            name = input("Enter your name: ")
            if name == ATM.SECRET_CODE:
                break
            pin = input("Enter your PIN: ")
            self._account = self._bank.get(pin)
            if self._account == None:
                print("Error, unrecognized PIN")
            elif self._account.getName() != name:
                print("Error, unrecognized name")
                self._account = None
            else:
                self._processAccount()

    def _processAccount(self):
        """A menu-driven command processor for a user."""
        while True:
            print("1  View your balance")
            print("2  Make a deposit")
            print("3  Make a withdrawal")
            print("4  Quit\n")
            number = input("Enter a number: ")
            theMethod = self._methods.get(number, None)
            if theMethod == None:
                print("Unrecognized number")
            else:
                theMethod()
                if self._account == None:
                    break

    def _getBalance(self):
        print("Your balance is $", self._account.getBalance())

    def _deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self._account.deposit(amount)

    def _withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        message = self._account.withdraw(amount)
        if message:
            print(message)

    def _quit(self):
        self._bank.save()
        self._account = None
        print("Have a nice day!")

# Top-level functions
def main():
    """Instantiate a Bank and an ATM and run it."""
    bank = Bank("bank.dat")
    atm = ATM(bank)
    atm.run()

def createBank(number = 0):
    """Saves a bank with the specified number of accounts.
    Used during testing."""
    bank = Bank()
    for i in range(number):
        bank.add(SavingsAccount('Name' + str(i + 1),
                                str(1000 + i),
                                100.00))
    bank.save("bank.dat")
