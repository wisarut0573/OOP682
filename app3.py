from models.student import Student
from models.classroom import Classroom

oop = Classroom("OOP")
oop.add_student(Student(1, "Alice", 20, "S1001"))
oop.add_student(Student(2, "Bob", 22, "S1002"))
print(f"{oop.name} registered {len(oop)} students")

oop.add_student(Student(3, "Charlie", 21, "S1003"))
print(len(oop))

for i in range(len(oop)):
    print(oop[i])