class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            print("Amount deposited:",amount)
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("Amount debited")
        else:
            print("Insufficient balance")
class atm(bankaccount):
    def show_details(self):
        print("      Account details     ")
        print("Name:", self.name)
        print("Balance:", self.get_balance())
acc=atm("Harini",90000)
acc.show_details()
acc.deposit(800)
acc.withdraw(700)
acc.show_details()
