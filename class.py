class student:
    def __init__(self,name,regno,department,mark,phoneno,city):
        self.name=name
        self.mark=mark
        self.regno=regno
        self.department=department
        self.phoneno=phoneno
        self.city=city
    def display(self):
        print("Student details")
        print("Name:",self.name)
        print("Register number:",self.regno)
        print("Department:",self.department)
        print("Marks:",self.mark)
        print("Phone number:",self.phoneno)
        print("City:",self.city)
s1=student("Harini",192319022,"BME",98,6380534848,"Chennai")
s2=student("Raksha",192319016,"BME",90,73986744,"Porur")
s3=student("Rahul",192319010,"BME",89,98786565,"Thiruvallur")
s1.display()
s2.display()
s3.display()