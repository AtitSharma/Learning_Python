
from cmath import cos, sin
import math
import numpy
# print(math.sin(0.45))
# a=0.466
# x=(numpy.arcsin(a))
# print(math.degrees(x))
# print(math.radians(x))

AB=int(input())
BC=int(input())
hipotenus1=((AB**2)+(BC**2))
ans=math.sqrt(hipotenus1)
# print(ans)
AM=ans/2
MC=ans/2
y=numpy.arcsin(AB/ans)
Angle_C=math.degrees(y)
# print(round(Angle_C))
ang=Angle_C

# ang = float(input("what's your angle ?: "))
the_divided_num = float(180 / ang)
x = math.cos(math.pi / the_divided_num) 
# print((x))

BM=math.sqrt(BC**2+MC**2-2*(BC*MC)*x)
print(BM)


angle_m=BC**2-((MC**2)+(BM**2))
dividede=(-2*MC*BM)
Angle=angle_m/dividede
# print(Angle)
Angle_M=numpy.arccos(Angle)
Final_Angle_M=(math.degrees(Angle_M))
# print(round(Angle_C))
Angle_B=180-Angle_C-Final_Angle_M
print(round(Angle_B))




# ang = float(input("what's your angle ?: "))
# the_divided_num = float(180 / ang)
# x = math.cos(math.pi / the_divided_num) 
# print((x))


