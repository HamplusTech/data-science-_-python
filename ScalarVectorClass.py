from math import sqrt

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y )
        else:
            return TypeError ("Expected Point but got %s" %type(other))
    
    def __sub__(self,other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y )
        else:
            return TypeError ("Expected Point but got %s" %type(other))
        
    def __mul__(self,other):
        if isinstance(other, Point):
            return (self.x * other.x + self.y * other.y )
        elif isinstance (other, int):
            return Point(self.x * other , self.y * other )
        else:
            return TypeError ("Expected Point or Int but got %s" %type(other))

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
