class Rectangle:
    def __init__(self,length,wedth):
        self.length=length
        self.wedth=wedth
    def Area_of_Rec(self):
        print(f"The Area of Rectangle is {self.length*self.wedth}")

class Square(Rectangle):
    def __init__(self,length,wedth):
        super().__init__(length,wedth)

    def Area(self):
        print(f"The Area of Square is {self.length*self.wedth}")

class Cube(Rectangle):
    def __init__(self,height,wedth,length):
        super().__init__(length,wedth)
        self.height=height

    def Volume(self):
        print(f"The Volume of Cube is {self.length*self.wedth*self.height}")


Rec=Rectangle(3,3)
Cub=Cube(3,3,3)
Cub.Volume()
Cub.Area_of_Rec()##CUBE CAN USE THE AREA OF RECTANGLE DUE TO SUPER FUNCTION
S=Square(1,2)
S.Area()


