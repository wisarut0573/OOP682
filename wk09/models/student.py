from models.person import Person

<<<<<<< HEAD

=======
>>>>>>> cc0e7ac70ad0b6d1f84436f8b9705ccc4b6d9d3f
class Student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.student_id = student_id

    def __str__(self):
<<<<<<< HEAD
        return f"Student[{self.pid}, {self.name}, {self.age}]"
=======
        return f"Student(ID: {self.pid}, Name: {self.name}, Age: {self.age}, StudentID: {self.student_id})"
>>>>>>> cc0e7ac70ad0b6d1f84436f8b9705ccc4b6d9d3f
