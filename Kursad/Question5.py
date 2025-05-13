# Question5 - Kursad

class Customer():
    def __init__(self, name, surname, tc_identification, phone ):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone
    
    def display_information(self):
        print(f"{self.name} {self.surname} {self.tc_identification} {self.phone}")

class Account(Customer):
    def __init__(self, customer, account_number, balance = 0):
        super().__init__(customer.name, 
                         customer.surname, 
                         customer.tc_identification, 
                         customer.phone)
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def money_check(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("not enough balance")

    def display_balance(self):
        print(f"Balance: {self.balance}")


customer1 = Customer("Ali",
                     "Kaya",
                     "12345678912",
                     "0687589657"
                     )

account = Account(customer1, "NLINGB3456789054332")

account.deposit(1000)
account.display_balance()
account.money_check(500)
account.display_balance()
account.money_check(600)
account.display_balance()

