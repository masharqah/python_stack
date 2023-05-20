# user balance classses
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def make_deposit(self, amount):	
        self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        
    def display_user_balance (self):
        print(self.account_balance)
        
    def transfer_money_to(self,amount, recepient):
        self.account_balance -= amount
        recepient.account_balance += amount
    
user1=User("Ahmad", "ahm@gmail.com")
user2=User("Ali", "Ali@gmail.com")
user3=User("Amjad","Amjad@fmsdf.com")

user1.make_deposit(300)
user1.make_deposit(100)
user1.make_deposit(55)
user1.make_withdrawal(300)
user1.display_user_balance()

user2.make_deposit(2000)
user2.make_deposit(10)
user2.make_withdrawal(500)
user2.make_withdrawal(300)
user2.display_user_balance()

user3.make_deposit(4000)
user3.make_withdrawal(200)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.display_user_balance()

user1.transfer_money_to(300, user3)

user1.display_user_balance()
user3.display_user_balance()