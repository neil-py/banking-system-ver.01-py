# user info: #
# name, gender, age, account_balance #

# Bank system: #
# deposit, withdraw, exit #

# Thank you for checking my code!! #
# You can contact me via email #
import time

# parent class #
class UserInfo():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def account_details(self):
        print(f"================================\nName: {self.name}\nGender: {self.gender}\nAge: {self.age} \
            \n================================")

# child class #
class BankSys(UserInfo):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.account_balance = 0
    
    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.account_balance += deposit_amount
        print(f"Updating account.... Depositing ${self.deposit_amount}....\n")
    
    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if withdraw_amount > self.account_balance: # if account balance is inssuficient for withdraw #
            print("Invalid Request! Insufficient funds\n")
            
        else:
            self.account_balance -= self.withdraw_amount
            print(f"Updating account.... Withdrawing ${self.withdraw_amount}....\n")

    def new_user_details(self):
        print("Account Updated!")
        self.account_details()
        print(f"Balance: ${self.account_balance}")
        

print("================================")
user = input("Enter your full name: ")
print("================================")
gender = input("Enter your gender: ")
print("================================")
age = int(input("Enter your age: "))
print("================================")
user_profile = UserInfo(user, gender, age)
time.sleep(0.5)
print("\nProcessing Details.....\n")
time.sleep(0.5)
user_profile.account_details() # prints initial user details #

def banking_system():

    bank_system = BankSys(user, gender, age)
    while True:
        user_choice = int(input("================================\nCommands:\nDeposit (1)\nWithdraw (2) \
            \nExit (3)\n================================\nInput: "))
        print("================================\n")
        
        deposit_amount_main = 0 # for deposit ammount #
        withdraw_amount_main = 0 # for withdraw ammount #

        # deposit #
        if user_choice == 1:
            deposit_ammount = int(input("Deposit ammount: $"))
            print("================================")
            deposit_amount_main += deposit_ammount
            new_balance_deposit = bank_system.deposit(deposit_amount_main)
            time.sleep(0.5)
            print("Deposit Successful!")
            print("================================")
            time.sleep(0.5)
            print("Updating Banking Details....\n")
            time.sleep(0.5)
            new_balance_deposit
            time.sleep(0.5)
            bank_system.new_user_details()

        # withdraw #
        if user_choice == 2:
            withdraw_ammount = int(input("Withdraw ammount: $"))
            print("================================")
            withdraw_amount_main += withdraw_ammount
            new_balance_withdraw = bank_system.withdraw(withdraw_amount_main)
            time.sleep(0.5)
            print("Deposit Successful!")
            print("================================")
            time.sleep(0.5)
            print("Updating Banking Details....\n")
            time.sleep(0.5)
            new_balance_withdraw
            time.sleep(0.5)
            bank_system.new_user_details()
        
        # exit #
        if user_choice == 3:
            print("\nExiting....\n")
            time.sleep(0.5)
            break

banking_system() # execute #
