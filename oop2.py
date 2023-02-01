
class Students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]

    def add_students(self,students):
        if len(self.students) < self.max_students:
            self.students.append(students)
            return True
        return False

    def get_average_grade(self):
        marks=0
        for student in self.students:
            marks+=student.get_grade()
        return marks/len(self.students)

s1=Students('Atit',20,90)
s2=Students('Ram',24,60)
s3=Students('Sam',10,10)

C=Course('Science',2)
C.add_students(s1)
C.add_students(s2)
C.add_students(s3)
print(C.get_average_grade())