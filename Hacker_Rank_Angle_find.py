import math
AB=int(input())
BC=int(input())
AC=math.sqrt(AB**2+BC**2)
angle_C=AB/AC
k=(math.asin(angle_C))
print(str(round(math.degrees(k)))+u'\N{DEGREE SIGN}')




