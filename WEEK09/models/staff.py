from models.person import Person

class Staff(Person):
    def __init__(self, pid, name, age, StaffID):
        super().__init__(pid, name, age)
        self.StaffID = StaffID

    def __str__(self):
        return f"Staff(ID: {self.pid}, Name: {self.name}, Age: {self.age}, StaffID: {self.StaffID})"