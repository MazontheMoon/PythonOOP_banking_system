'''
SD-GAL-05 SD-TA-007-A Task 3
Author: Mary Ronan
Creation Date: 30/01/2026
'''

# Required imports
from abc import ABC, abstractmethod
import datetime
import unittest

# Parent Class
class Account(ABC):

    # Class Attributes
    transactionType = ""
    amount = 0.0

    # Class Instance
    def __init__(self, accountNumber, accountBalance):
        self.accountNumber = accountNumber
        self.accountBalance = accountBalance

    # Class Getter Functions
    def getAccountNumber(self):
        return self.accountNumber

    # Class Methods

    # Withdraw
    def withdraw(self):
        self.amount = float(input("Enter Withdrawal Amount: €"))
        self.accountBalance = self.accountBalance - self.amount

    # Deposit
    def deposit(self):
        self.amount = float(input("Enter Deposit Amount: €"))
        self.accountBalance = self.accountBalance + self.amount

    # Get Balance
    def checkBalance(self):
        return self.accountBalance

    # Get Transaction Type
    def getTransaction(self):
        self.transactionType = input("Enter [D] to make a Deposit\nEnter [W] to make a Withdrawal\nEnter [B] to check the balance:").upper()
        if self.transactionType == "D":
            self.transactionType = "Deposit"
            self.deposit()
        elif self.transactionType == "W":
            self.transactionType = "Withdrawal"
            self.withdraw()
        else:
            self.transactionType = "Check Balance"

    def getTransactionType(self):
        return self.transactionType
                            
    # Display Greeting
    def displayWelcomeMessage():
        print("-".ljust(70, "-"))
        print("Fortuna Investments & Trading Ltd.".center(50))
        print("Banking System".center(50))
        print("-".ljust(70, "-"))

    # Display Exit Message
    def displayExitMessage():
        print("-".ljust(70, "-"))
        print("Thank you for using Fortuna Investments & Trading Ltd. Banking System".center(50))
        print("-".ljust(70, "-"))

    # Generate Timestamp
    def getTimeStamp(self):
        return datetime.datetime.now().strftime("%c")

    # Abstract Methods
    @abstractmethod
    def printDetails(self):
        print("*".ljust(55, "*"))
        print("Account Information".center(50))
        print("*".ljust(55, "*"))
        print("Account Number".ljust(25),": ", self.getAccountNumber())
        print("Balance".ljust(25),": €", self.checkBalance())

# Child Class
class Savings(Account):

    # Class Attributes
    interestRate = 0.95

    # Class Instance
    def __init__(self, accountNumber, accountBalance):
        super().__init__(accountNumber, accountBalance)

    # Class Getter Functions
    def getInterestRate(self):
        return str(self.interestRate) + "%"
    
    # Calculate Interest
    def calcInterest(self):
        return (self.accountBalance * self.interestRate) / 100

    # Display details on screen
    def printDetails(self):
        super().printDetails()
        print("*".ljust(55, "*"))
        print("Account Type".ljust(25),":", "Savings")
        print("Interest Rate".ljust(25),":", self.getInterestRate())
        print("Annual Interest Amount".ljust(25),": €", self.calcInterest())
        print("Transaction Type".ljust(25),":", self.getTransactionType() , "€" , self.amount)
        print("Transaction Date".ljust(25),":",self.getTimeStamp())
        print("*".ljust(55, "*"))

# Child Class
class Current(Account):

    # Class Attributes
    transactionFee = 0.55

    # Class Instance
    def __init__(self, accountNumber, accountBalance):
        super().__init__(accountNumber, accountBalance)

    # Calculate Transaction Fee
    def calcTransactionFee(self):
        return self.accountBalance - self.transactionFee

    # Display details on screen
    def printDetails(self):
        super().printDetails()
        print("*".ljust(55, "*"))
        print("Account Type".ljust(25),":", "Current")
        print("Transaction Type".ljust(25),":", self.getTransactionType() , "€" , self.amount)
        print("Transaction Date".ljust(25),":",self.getTimeStamp())
        print("*".ljust(55, "*"))

# MAIN PROGRAM

# Display Greeting
Account.displayWelcomeMessage()

# Get User Input
accountType = input("Enter [S] for a Savings Account or Enter [C] for a Current Account: ").upper()
accountNumber = input("Enter Account Number: ")
accountBalance = float(input("Enter Account Balance: "))

if accountType == "S":
    account = Savings(accountNumber, accountBalance)
    account.getTransaction()
    account.printDetails()
else:
    account = Current(accountNumber, accountBalance)
    account.getTransaction()
    account.calcTransactionFee()
    account.printDetails()

# Display Exit Message
Account.displayExitMessage()

# Unit Testing
class unittests(unittest.TestCase):

    # Test 001 - Check account number is not blank
    def test001(self):
        assert account.getAccountNumber != ""

    # Test 002 - Check account is instance of Savings class

    def test002(self):
        if accountType == "S":
            self.assertIsInstance(account, Savings)

    # Test 003 - Check account is instance of Current class
def test003(self):
        if accountType == "C":
            self.assertIsInstance(payment, Current)

    # Test 004 - Check transaction amount is greater than 0.0
    def test004(self):
        if account.transactionType != "Check Balance":
            assert account.amount > 0.0
        
unittest.main()
