<<<<<<< HEAD
class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
    
=======
class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []

>>>>>>> cc0e7ac70ad0b6d1f84436f8b9705ccc4b6d9d3f
    def add_student(self, student):
        self.students.append(student)

    def __len__(self):
        return len(self.students)
<<<<<<< HEAD

=======
    
>>>>>>> cc0e7ac70ad0b6d1f84436f8b9705ccc4b6d9d3f
    def __getitem__(self, index):
        return self.students[index]