class cart:
    def __init__(self):
        self.total=0
    def add(self,price):
        self.total=price
    def show(self):
        print("Price",self.total)
c=cart()
c.add(100)
c.add(900)
c.show()