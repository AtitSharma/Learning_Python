class Person:
    def __init__(self,height,weight,color,salary):
        self.height=height
        self.weight=weight
        self.color=color
        self.salary=salary
    def Atit(self):
        
        print(f"I am a good boy{self.height}")


class Person2(Person):
    def __init__(self,weight,color,gender,salary):
        super().__init__(weight,color,salary,salary)
        self.gender=gender
        
    def Gender(self):
        print(f"The gender of the person2 is {self.gender}")




P=Person("2.5m",65,"brown",10000)
print(P.color)
P2=Person2(30,"brown","male",10000)
P2.Gender()
P.Atit()







