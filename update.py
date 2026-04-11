class students:
    def __init__(self,mark):
        self.mark=mark
    def update(self,new_mark):
        self.mark=new_mark
    def show(self):
        print("Mark:",self.mark)
s1=students(90)
s1.show()
s1.update(80)
s1.show()