class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def details(self):
        print(f'I am {self.name} . I am {self.age} years old . My grade is {self.grade}.')


s1 = Student("Adeel" , 21 , "B")
s2 = Student("Mukkaram" , 22 , "F")
s3 = Student("Asad" , 41 , "A")
s4 = Student("Arsal" , 23 , "C")

s1.details()
s2.details()
s3.details()
s4.details()