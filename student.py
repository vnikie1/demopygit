

class Student:
    school = "NGLIPS"

    def __init__(self, m1=0,m2=0,m3=0):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.laptop = self.Laptop()

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("Just info")

    class Laptop:
        def __init__(self, brand = "Dell", processor = "AMD"):
            self.brand = brand
            self.processor = processor

        def show(self):
            print(self.brand, self.processor , sep= "----")


s1 = Student(34,34,67)
s2 = Student(67,78,23)

print(s1.m1)
print(s2.m1)
lap1 = Student.Laptop("Lenovo" , "Intel")
print(id(lap1))
s1.laptop = lap1
print(id(s1.laptop))
print(id(s2.laptop))
print(s1.laptop.show())