class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def get_marks(self):
        print(str(self.m1) + " " + str(self.m2))

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return  s3

    def __str__(self):
        return "{} {} ".format(self.m1 , self.m2)

    def __gt__(self, other):
        if (self.m1 + self.m2) > (other.m1 + other.m2):
            return True
        else:
            return False



s2 = Student(98,67)
s1 = Student(45,34)
print(s1)
print(s2)
s3 = s1 + s2
print(s3)
if s1>s2:
    print("s1 has higher marks")
else:
    print("s2 has higher marks")
s3.get_marks()

