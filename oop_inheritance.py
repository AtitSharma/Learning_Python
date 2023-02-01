class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"I am {self.name} and I  am  {self.age} years old")

    def speak1(self):
        print(f"I am {self.name} and I donot speak")


class Dog(Pet):
    
    def speak(self):
        print(f"Bow Bow")


class Cat(Pet):
    def __init__ (self,name,age,color):
        super().__init__(name,age)
        self.color=color
    def speak(self):
        print(f"Meow")
    def show(self):
        print(f"I am {self.name} and I  am  {self.age} years old and i am {self.color} color")


P=Pet('Jackie',20)
D=Dog("Ram",22)
D.show()
c=Cat("Lucy",2222,'Green')
c.show()
c.speak1()