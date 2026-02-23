class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} is {self.age} years old.")

    def __str__(self):
<<<<<<< HEAD
        return f"{self.name} is {self.age} years."

def main():
    my_dog = Dog("Buddy", 3)
    your_dog = Dog("Paulie", 2)
    print(my_dog)

if __name__ == "__main__":
    main()
=======
        return f"Dog(Name: {self.name}, Age: {self.age})"
def main():
    my_dog = Dog("Buddy", 3)
    your_dog = Dog("Max", 5)
    print(my_dog)
  


if __name__ == "__main__":
    main()
>>>>>>> cc0e7ac70ad0b6d1f84436f8b9705ccc4b6d9d3f
