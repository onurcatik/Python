class Shape:
    def __init__ (self , color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        return f"Color: {self.color}, Filled: {'Yes' if self.is_filled else 'No'}"


class Circle(Shape):
    def __init__ (self, color , is_filled , radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__ (self, color ,is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
class Triangle(Shape):
    def __init__ (self , color , is_filled, width, height):
        super().__init__(color , is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled=True, radius=5)
print(f"Circle: Color={circle.color}, Is Filled={circle.is_filled}, Radius={circle.radius} cm")

# Creating a Square object
square = Square(color="blue", is_filled=False, width=6)
print(f"Square: Color={square.color}, Is Filled={square.is_filled}, Width={square.width} cm")

# Creating a Triangle object
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)
print(f"Triangle: Color={triangle.color}, Is Filled={triangle.is_filled}, Width={triangle.width} cm, Height={triangle.height} cm")


# -----------------

class Circle(Shape):
    def __init__ (self, color , is_filled , radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        description = super().describe()
        return f"{description}, Radius: {self.radius} cm"
    
class Square(Shape):
    def __init__(self, color, is_filled , width):
        super().__init__(color, is_filled)
        self.width = width
    
    
    def describe(self):
        description = super().describe()
        return f"{description}, Width: {self.width} cm"
    
class Triangle(Shape):
    def __init__(self, color, is_filled,width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        description = super().describe()
        return f"{description}, Width: {self.width} cm, Height: {self.height} cm"
        

    
print(circle.describe())
print(square.describe())
print(triangle.describe())