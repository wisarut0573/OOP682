from models.person import Person

class Staff(Person):
<<<<<<< HEAD
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)
        self.staff_id = staff_id

    def __str__(self):
        return f"Staff[{self.pid}, {self.name}, {self.age}]"
=======
    def __init__(self, pid, name, age, StaffID):
        super().__init__(pid, name, age)
        self.StaffID = StaffID

    def __str__(self):
        return f"Staff(ID: {self.pid}, Name: {self.name}, Age: {self.age}, StaffID: {self.StaffID})"
>>>>>>> cc0e7ac70ad0b6d1f84436f8b9705ccc4b6d9d3f
