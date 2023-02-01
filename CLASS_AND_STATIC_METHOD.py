class Person:
    Height1=100
    def __init__(self,age,name,height):
        self.name=name
        self.age=age
        self.height=height
    @classmethod
    def Height(cls):
        return (f"The height of the person is and {cls.Height1}")

    @staticmethod
    def Age(age):
        return(f"The age of the person is  {age}")

P=Person("Atit","100m",90)
print(Person.Height())
print(Person.Age(10))


