class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Cluster(object):
    def __init__(self, x, y):
        self.center = Point(x, y)
        self.points = []

    def __repr__ (self):
        return f'[Point({self.x},{self.y})]'
    
    def update(self):
        total = [0,0]
        for point in self.points:
            total[0] = total[0] + point.x
            total[1] = total[1] + point.y
        csum = total
        length = float(len(self.points))
        self.center = Point(csum.x/length, csum.y/length)
        self.points = []
    
    def add_point(self, point):
        self.point.append(point)

    def compute_result(points):
        points = [Point (*points) for point in points]
        a = Cluster(1,0)
        b = Cluster(-1,0)
        a_old = []
        for _ in range(10000):
            for point in points:
                if point.distance(a.center) < point.distance(b.center):
                    a.add_point(point)
                else:
                    b.add_point(point)
            if a_old == a.points:
                break
            a_old = [i for i in a.points]
            a.update()
            b.update()
        return ((a.center.x, a.center.y),
                    (b.center.x, b.center.y))
