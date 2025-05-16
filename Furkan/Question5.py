# Question5 - Furkan
class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"Customer Information: {self.name} {self.surname}, TC: {self.tc_identification}, Phone: {self.phone}")

class Account(Customer):
    def __init__(self, customer, account_number, balance=0):
        super().__init__(customer.name, customer.surname, customer.tc_identification, customer.phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

customer1 = Customer("Ayşe", "Yılmaz", "98765432109", "05321234567")
account = Account(customer1, "TRXINGB123456789012345", 500)
account.deposit(1500)
account.display_balance()
account.withdraw(700)
account.display_balance()
account.withdraw(1400)
account.display_balance()
