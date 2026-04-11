class ticket:
    def __init__(self,price):
        self.price=price
    def total(self,persons):
        print("Total",self.price*persons)
b=ticket(90)
b.total(9)