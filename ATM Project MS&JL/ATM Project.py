#Names: Jake Lee & Mohammed Shatit
#Date: 6/28/19
#Description: ATM Semester project using a base class


#Welcome message
print("Welcome to the MCC ATM")


#Base class
class ATM:
    def __init__(self, userPin):
        self.userPin = userPin
        self.pin = "1234"
        self.savings = 1000
        self.checking = 1000

        #Parallel lists; 1 containing strings parallel to 1 containing numbers
        self.descriptions = []
        self.amounts = []

    #Checking user's choice to advance from main menu
    def runATM(self):
        self.printMenu()
        userChoice = int(input("Choice==> "))
        while userChoice != 6:
            if userChoice == 1:
                self.getBalance()
            elif userChoice == 2:
                self.deposit()
            elif userChoice == 3:
                self.withdraw()
            elif userChoice == 4:
                self.transfer()
            elif userChoice == 5:
                self.printHistory()
            else:
                print()
                print("***Invalid Entry***")
                
            self.printMenu()
            userChoice = int(input("Choice==> "))

    #Checking and declaring if user enters correct, or incorrect pin number
    def checkPin(self):
        OkToRun = False
        numGuess = 0
        if self.userPin == self.pin:
            print("Correct pin, thank you!")
            OkToRun = True
        else:
            numGuess += 1
            while numGuess < 3:
                self.userPin = input("Incorrect pin, please try again: ")
                if self.userPin == self.pin:
                    print("Correct Pin, Thank You!")
                    OkToRun = True
                    break
                else:
                    numGuess += 1
        return OkToRun

    #Main menu that user refers back to, printing options to advance
    def printMenu(self):
        print("****************************************")
        print("1: Balance Inquiry")
        print("2: Deposit Funds")
        print("3: Withdrawl Funds")
        print("4: Transfer Funds")
        print("5: History of Last 5 Transactions")
        print("6: Exit")
        print("****************************************")

    #Getting balance & adding to .descriptions string list & .amounts number list
    def getBalance(self):
        print("Checking Balance: $", format(self.checking, ",.2f"), sep = "")
        print("Savings Balance: $", format(self.savings, ",.2f"), sep = "")
        self.descriptions.append("Balance Inquiry")
        self.amounts.append("")

    #Taking user's choice amount and depositing to user's choice of account
    def deposit(self):
        print("****************************************")
        print("1: Checking")
        print("2: Savings")
        print("3: Back")
        print("****************************************")
        userChoice = int(input("Choice==> "))
        if userChoice == 1:
            userAmount = float(input("Enter amount to deposit:  "))
            self.checking += userAmount
            self.descriptions.append("Deposit to Checking account")
            self.amounts.append(format(userAmount, ',.2f'))
        elif userChoice == 2:
            userAmount = float(input("Enter amount to deposit:  "))
            self.savings += userAmount
            self.descriptions.append("Deposit to Savings account")
            self.amounts.append(format(userAmount, ',.2f'))
        elif userChoice == 3:
            print()
        else:
            print()
            print("Invalid Entry")


    #Withdrawing user's available amount from user's choice of account if amount is available
    def withdraw(self):
        flag = False
        print("****************************************")
        print("1: Checking")
        print("2: Savings")
        print("3: Back")
        print("****************************************")
        userChoice = int(input("Choice==> "))
        if userChoice == 1:
            userAmount = int(input("Enter amount to withdraw: "))
            while flag == False:
                if userAmount <= self.checking:
                    if userAmount % 10 != 0:
                        userAmount = int(input("Withdrawals Amounts must be in denomination of 10"))
                    else:
                        self.checking -= userAmount
                        self.descriptions.append("Withdrawl from Checking account")
                        self.amounts.append(format(userAmount, ',.2f'))
                        flag == True
                        break
                else:
                    print()
                    userAmount = int(input("Not Sufficient Amount To Withdraw. Try Again: "))

        elif userChoice == 2:
            userAmount = int(input("Enter amount to withdraw: "))
            while flag == False:
                if userAmount <= self.savings:
                    if userAmount % 10 != 0:
                        userAmount = int(input("Withdrawals Amounts must be in denomination of 10"))
                    else:
                        self.savings -= userAmount
                        self.descriptions.append("Withdrawl from Savings account")
                        self.amounts.append(format(userAmount, ',.2f'))
                        flag == True
                        break
                else:
                    print()
                    userAmount = int(input("Not Sufficient Amount To Withdraw. Try Again: "))

        elif userChoice == 3:
            print()
        else:
            print()
            print("Invalid Entry")


    #Transferring funds from 1 account to another account according to user's choice
    def transfer(self):
        flag = False
        print("****************************************")
        print("1: Transfer To Checking Account")
        print("2: Transfer To Savings Account")
        print("3: Back")
        print("****************************************")
        userChoice = int(input("Choice==> "))
        if userChoice == 1:
            userAmount = int(input("Enter amount to Transfer: "))
            while flag == False:
                if userAmount <= self.savings:
                    self.descriptions.append("Transfer To Checking account")
                    self.amounts.append(format(userAmount, ',.2f'))
                    self.checking += userAmount
                    self.savings -= userAmount
                    flag == True
                    break
                else:
                    print()
                    userAmount = int(input("Not Sufficient Amount To Transfer. Try Again: "))
        elif userChoice == 2:
            userAmount = int(input("Enter amount to Transfer: "))
            while flag == False:
                if userAmount <= self.checking:
                    self.descriptions.append("Transfer To Savings account")
                    self.amounts.append(format(userAmount, ',.2f'))
                    self.checking -= userAmount
                    self.savings += userAmount
                    flag == True
                    break
                else:
                    print()
                    userAmount = int(input("Not sufficient amount to transfer. Try again: "))

        elif userChoice == 3:
            print()
        else:
            print()
            print("Invalid Entry")


    #Prints history of last 5 transactions, unless user does not make 5 or more transactions
    def printHistory(self):
        print("\n")
        print("Transaction History")
        print("-------------------")
        counter = 1
        if len(self.descriptions) > 4:
            for i in range(len(self.descriptions) - 1, len(self.descriptions) - 6, -1):
                print(counter,".", self.descriptions[i], " $", self.amounts[i], sep = "")
                counter += 1
        else:
            print("Not enough transactions to show.")

        print("\n")

#main
def main():
    userPin = input("Enter the pin: ")
    ATM1 = ATM(userPin)
    isPinOK = ATM1.checkPin()
    if isPinOK == True:
        ATM1.runATM()
    else:
        print("Thank you & come again...")

#Calling to main
main()
