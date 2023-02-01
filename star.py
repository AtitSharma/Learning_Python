class Bijay:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def Hancy(self):
        print(f"{self.name} is {self.age} years old")

class Atit(Bijay):
    def __init__(self,hero):
        self.hero=hero

        super().__init__('Atit',24)
            
    def Hancy2(self):
        print(f"{self.name} is {self.age} years old and he is {self.hero}")

P1=Bijay('Bijay','23')
A1=Atit('Raila')
A1.Hancy2()
P1.Hancy()




        
