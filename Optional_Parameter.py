# def Optional(num,add,power=1):
#     return (num*(add+power))
# print(Optional(True,2))



class Car:
    def __init__(self,name,model,speed,condition,kms):
        self.name=name
        self.model=model
        self.speed=speed
        self.condition=condition
        self.kms=kms
    def CarInfo(self,showall=True):
        if showall:
            print(f"The {self.name} is faltastic and of model {self.model} and its speed is {self.speed} and its condition is {self.condition},its speed is {self.speed}")
        else:
            print("Nop")
class Cycle(Car):
    population=100
    def __init__(self,name,model,speed,condition,kms,modell):
        super().__init__(name,model,speed,condition,kms)
        self.modell=modell

    @classmethod
    def Cycle2(cls):
        return(f"This is population  of company is {cls.population}")

    @staticmethod
    def Isage(age):
        return age>=18
        

C1=Car("Bugatti",900,900,"New",1000)
C1.CarInfo(True)
Cy=Cycle("Bugatti",900,900,"New",1000,"Lambo")
Cy.Cycle2()

print(Cycle.Cycle2())
print(Cycle.Isage(91))