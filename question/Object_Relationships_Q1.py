# ---------------------------------------------------------------------
# 
# File          : Object_Relationships_Q1.py  
# Created       : 31/10/2021 12:43
# Authort       : Lukasz S.
# Version       : v1.0.0
# Licencing     : (C) 2021 Lukasz S.
#
# Description   :
# ---------------------------------------------------------------------


class Person:
    def __init__(self,name,markCA, lecture):
        self.name = name
        self.markCA = markCA
        self.lecture = lecture
    def display(self):
        print('Name: ', self.name)
        print('markCA: ', self.markCA)
        print('lecture: ', self.lecture)


class Student(Person):
    def __init__(self, name, markCA, lecture, attendCollege, sitExams):
       super().__init__(name, markCA, lecture)
       self.attendCollege = attendCollege
       self.sitExams = sitExams


    def display(self):
        Person.display(self)
        print('Attend College: ', self.attendCollege)
        print('Sit Exams: ', self.sitExams)


s1=Student ('Filip','55%', 'Python', 'LIYT',"yes" )

s2=Student ('Teri','77%','Privet Cloud', 'LIYT', 'no')

print('Student Details: ')
s1.display()
print('\n')
s2.display()



