class Person:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age
<<<<<<< HEAD

    def __str__(self):
        return f"Person[{self.pid}, {self.name}, {self.age}]"
=======
        
    def __str__(self):
        return f"Person(ID: {self.pid}, Name: {self.name}, Age: {self.age})"
>>>>>>> cc0e7ac70ad0b6d1f84436f8b9705ccc4b6d9d3f
