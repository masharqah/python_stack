# user balance classses
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
        
    def display_user_balance (self):
        print(self.account_balance)
        return self
    def transfer_money_to(self,amount, recepient):
        self.account_balance -= amount
        recepient.account_balance += amount
        return self
    
user1=User("Ahmad", "ahm@gmail.com")
user2=User("Ali", "Ali@gmail.com")
user3=User("Amjad","Amjad@fmsdf.com")

user1.make_deposit(300).make_deposit(100).make_deposit(55).make_withdrawal(300).display_user_balance()
user2.make_deposit(2000).make_deposit(10).make_withdrawal(500).make_withdrawal(300).display_user_balance()
user3.make_deposit(4000).make_withdrawal(200).make_withdrawal(100).make_withdrawal(100).display_user_balance()


user1.transfer_money_to(300, user3).display_user_balance()
user3.display_user_balance()