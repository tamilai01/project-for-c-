class Parent():
    def __init__(self):
        print("family name is bright services")
        
    def AadharAccess(self):
        print("Need Aadhar Access")
    def classroom(self):
        print("You can access Class room")
    def lab01(self):
        print("you can access lab 01")
    def lab02(self):
        print("you can access lab02")
    def aibatch(self):
        print("you can join AI course")
    def cadbatch(self):
        print("your can join Cloud application developer course")
    def nightshiftwork(self):
        print("you can join to work in the us process for us work timing")

class aibatch(Parent):
    def __init__(self):
        super().__init__()
        super().AadharAccess()
        super().lab01()
        super().lab02()
        super().aibatch()
        super().classroom()
        print("welcome to Aibatch")
    def C(self):
        print("i can study c")
    def cpp(self):
        print("i can study c++")
    
    def python(self):
        print("i can study python")


class cadbatch(Parent):
    def __init__(self):
        super().__init__()
        super().AadharAccess()
        super().lab01()
        super().lab02()
        super().classroom()
        super().cadbatch()
        print("welcome to cadbatch")
    def html(self):
        print("i can study html")
    def javascript(self):
        print("i can study javascript")
    
    def csharp(self):
        print("i can study C#")


        
    



# ai=aibatch()

cad=cadbatch()
