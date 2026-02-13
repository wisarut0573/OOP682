from abc import  abstractmethod

class Shape:#รูปร่าง
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):#วงกลม
    def __init__(self, radius: float):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):#สี่เหลี่ยมผืนผ้า
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

def calculate_area(shape):#คำนวณพื้นที่
    return shape.area()