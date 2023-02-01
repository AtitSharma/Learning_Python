class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # print(name)


    def get_age(self):
        return (f"The age is  {self.age}")
    
    def get_name(self):
        return (f"The name is {self.name}")
        

    def set_age(self,age):
        self.age=age







    # def Bark(self):
    #     print( "Bhau Bhau")
    # def add_Func(self,x):
    #     return x+1

d1=Dog('Kitti',15)
# print(d.add_Func(5))
# d.Bark()
# print(d1.name)
# print(d2.name)
d1.set_age(100)
print(d1.get_name())
print(d1.get_age())
