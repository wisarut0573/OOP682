<<<<<<< HEAD
from models.classroom import ClassRoom
from models.student import Student


oop = ClassRoom("OOP")
oop.add_student(Student(1, "Alice", 20, "S001"))
oop.add_student(Student(2, "Bob", 22, "S002"))
print(f'{oop.name} registered {len(oop)} students')
oop.add_student(Student(3, "Charlie", 21, "S003"))
print(len(oop))
print('Students in the class:')
=======
from models.student import Student
from models.classroom import Classroom

oop = Classroom("OOP")
oop.add_student(Student(1, "Alice", 20, "S1001"))
oop.add_student(Student(2, "Bob", 22, "S1002"))
print(f"{oop.name} registered {len(oop)} students")

oop.add_student(Student(3, "Charlie", 21, "S1003"))
print(len(oop))

>>>>>>> cc0e7ac70ad0b6d1f84436f8b9705ccc4b6d9d3f
for i in range(len(oop)):
    print(oop[i])