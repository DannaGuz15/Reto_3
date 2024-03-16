import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def compute_length(self):
        return math.sqrt((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)
    
    def compute_slope(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        return math.degrees(math.atan2(dy, dx))
    
    def compute_horizontal_cross(self):
        return self.start.y == 0 or self.end.y == 0
    
    def compute_vertical_cross(self):
        return self.start.x == 0 or self.end.x == 0

class Rectangle:
    def __init__(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        
        self.top_line = Line(top, right)
        self.right_line = Line(right, bottom)
        self.bottom_line = Line(bottom, left)
        self.left_line = Line(left, top)

top_left = Point(0, 7)
top_right = Point(3, 4)
bottom_left = Point(0, 0)
bottom_right = Point(6, 0)

rectangle = Rectangle(top_left, top_right, bottom_right, bottom_left)

print("Rectangle Top Line Slope:", rectangle.top_line.compute_slope())
print("Rectangle Right Line Length:", rectangle.right_line.compute_length())





