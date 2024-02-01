#PARENT CLASS
class User():
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)




class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance=0
       
    
    def deposit(self, amount):
        self.balance = self.balance+amount
        print(f"Balance updated to {self.balance}")
    
    def withdraw(self, amount):
        
        if (amount>self.balance):
            print("Insufficient Funds")
        else:
            self.balance = self.balance-amount
            print(f"Balance updated to  ${self.balance}")
        
    def view_balance(self):
        self.show_details()
        print(f"Account balance: ${self.balance}")



object_Name = Bank("Robert Bob", 21, 'Male')
object_Name.show_details()
object_Name.deposit(300)
print(object_Name.balance)
object_Name.deposit(200)
object_Name.withdraw(400)
object_Name.view_balance()