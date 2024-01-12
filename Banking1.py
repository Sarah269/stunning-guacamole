#  Object-oriented programming
# Banking

# Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Personal Details")
        print ("Name: ", self.name)
        print ("Age: ", self.age)
        print ("Gender: ", self.gender)
        
# Child Class
# Inherit all properties and methods from User class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
        self.depsum = 0
        self.depcnt = 0
        self.wtdsum = 0
        self.wtdcnt = 0
        
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        self.depsum = self.depsum + self.amount
        self.depcnt = self.depcnt + 1
        # print("\n")
        print("Customer Name: ", self.name)
        print("$", self.amount, "deposit complete. New balance: $", self.balance)
    
    def withdrawal(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            # print("\n")
            print("Customer Name: ", self.name)
            print(f'Withdrawal request for $ {self.amount}. Insufficient funds.  Balance available is $ {self.balance}')
        else:
            self.balance = self.balance - self.amount
            self.wtdsum = self.wtdsum + amount
            self.wtdcnt = self.wtdcnt + 1
           
            print("Customer Name: ", self.name)
            print("$", self.amount, "withdrawal complete. New balance: $", self.balance)
           
    
    def view_balance(self):
        print("\n")
        print("Customer Name: ", self.name)
        print("Account balance is $", self.balance, "\n")
             
    def activity(self):
        print("\n")
        print("Transaction Report for: ", self.name)
        print("Account balance ($):  ", self.balance)
        print("Number of deposits: ", self.depcnt, ". Total Deposited ($): ", self.depsum)
        print("Number of withdrawals: ", self.wtdcnt,". Total Withdrawn ($): ", self.wtdsum )
         
        
lisa = Bank("Lisa",35,"female")
lisa.view_balance()
lisa.deposit(357)
lisa.withdrawal(500)
lisa.deposit(1500)
lisa.deposit(750)
lisa.withdrawal(375)
lisa.activity()

Harry = Bank("Harry",45,"male")
Harry.view_balance()
Harry.deposit(250)
Harry.withdrawal(750)
Harry.deposit(2500)
Harry.withdrawal(500)
Harry.deposit(500)
Harry.withdrawal(240)
Harry.activity()