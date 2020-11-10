class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Cluster():
    def __init__(self, x, y):
        self.center = Point(x, y)
        self.points = []

    def update(self):
        x_c = sum(point.x for point in self.points)/len(self.points) 
        y_c = sum(point.y for point in self.points)/len(self.points)
        self.center = Point(x_c, y_c)

    def add_point(self, point):
        self.points.append(point)

    def __repr__(self):
        return "Point(%d, %d)" % (self.center.x , self.center.y)


def compute_result(points):
    points = [Point(*point) for point in points]
    a = Cluster(1,0)
    b = Cluster(-1,0)
    a_old = []
    for _ in range(10000): # max iterations
        a.points = [ ]
        b.points = [ ]
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                # add the right point
                a.add_point(point)
                #  print("1")
            else:
                # add the right point
                b.add_point(point)
                #print("2")

        if a_old == a.points:
            print("3")
            #print(a.points)
            #print(b.points)
            break
        a_old = a.points
        a.update()
        #print("4")
        b.update()
        #print("5")
        mylistoftuples = [(a.center.x, a.center.y), (b.center.x, b.center.y)]
        return mylistoftuples
