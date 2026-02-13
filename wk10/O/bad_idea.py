class Circle:#วงกลม
    def __init__(self, radius: float):
        self.radius = radius

class Rectangle:#สี่เหลี่ยมผืนผ้า
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

def calculate_area(shape):#คำนวณพื้นที่
    if isinstance(shape, Circle):
        return 3.14159 * shape.radius ** 2
    elif isinstance(shape, Rectangle):
        return shape.width * shape.height
    else:
        raise ValueError("Unknown shape")
    