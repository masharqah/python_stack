class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print( "Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print ("Balance: ", self.balance)
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance += (self.balance*self.int_rate)
        return self
# user balance classses
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts=[]

    def create_account(self, int_rate=0.0, balance=0.0):
        added_account = BankAccount(int_rate, balance)
        self.accounts.append(added_account)
        
    def make_deposit(self, account_index, amount):
        self.accounts[account_index].deposit(amount)
        return self

    def make_withdrawal(self,account_index, amount):
        self.accounts[account_index].withdraw(amount)
        return self
        
    def display_user_balance (self, account_index):
        self.accounts[account_index].display_account_info()
        return self

    def transfer_money_to(self, amount, account_index_sender,  recepient, account_index_recepient):
        self.accounts[account_index_sender].withdraw(amount)
        recepient.accounts[account_index_recepient].deposit(amount)

Ahmad=User("Ahmad","Email@email.com")
Ahmad.create_account(0.03, 1000)
Ahmad.create_account(0.01, 2000)
Ahmad.make_deposit(0, 500).display_user_balance(0)
Ali=User ("Ali", "Ali@mail.com")
Ali.create_account(0.03, 500)
Ahmad.transfer_money_to(600,1,Ali,0)
Ali.display_user_balance(0)