class Person:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, pid, name, age, StudentID):
        super().__init__(pid, name, age)
        self.StudentID = StudentID
    
class Staff(Person):
    def __init__(self, pid, name, age, StaffID):
        super().__init__(pid, name, age)
        self.StaffID = StaffID

Std1 = Student(1160102356924, "Alice", 20, "S123")
St1 = Staff(1023624325623, "Bob", 35, "T456")   
print(f"Student: {Std1.name}, ID: {Std1.StudentID}")
print(f"Staff: {St1.name}, ID: {St1.StaffID}")