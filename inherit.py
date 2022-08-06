class A:

    def __init__(self):
        print("in init of A")

    def feature1(self):
        print("Class A Feature 1")

    def feature2(self):
        print("Class A Feature 2")


class B:
    def __init__(self):
        #super().__init__()
        print("in init of B")

    def feature3(self):
        print("Class B Feature 3")

    def feature4(self):
        print("Class B Feature 4")


class C(B, A):

    def __init__(self):
        super().__init__()
        print("in init of C")


# a1 = A()
b1 = C()
b1.feature3()
