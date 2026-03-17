import math


class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}/{self.y})"

    def __repr__(self):
        return f"({self.x}/{self.y})"

    def distance_from_origin(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Shape(list):

    def __init__(self, *points: Point):
        super().__init__(points)

    def __str__(self):
        return f"Shape {list(self)}"

    def __repr__(self):
        return f"{list(self)}"

    def centroid(self) -> Point:
        n = len(self)
        avg_x = sum(p.x for p in self) / n
        avg_y = sum(p.y for p in self) / n
        return Point(avg_x, avg_y)

    def __eq__(self, other):
        return self.centroid().distance_from_origin() == other.centroid().distance_from_origin()

    def __lt__(self, other):
        return self.centroid().distance_from_origin() < other.centroid().distance_from_origin()


# Quick tests
p1 = Point(2.3, 43.14)
p2 = Point(5.53, 2.5)
p3 = Point(12.2, 28.7)
print(p1)
print([p1, p2, p3])

s1 = Shape(p1, p2, p3)
s2 = Shape(p2)
s3 = Shape()
print(s1)
print(s2)
print(s3)

# centroid test
s1 = Shape(Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0))
s2 = Shape(Point(0, 0.5), Point(0.5, 1), Point(1, 0.5), Point(0.5, 0))
s3 = Shape(Point(0.25, 0.25), Point(0.25, 0.75), Point(0.75, 0.75), Point(0.75, 0.25))
print(s1.centroid())
print(s2.centroid())
print(s3.centroid())

# distance test
p1 = Point(1, 1)
p2 = Point(5, 5)
p3 = Point(10, 10)
print(p1.distance_from_origin())
print(p2.distance_from_origin())
print(p3.distance_from_origin())

# comparison test
s1 = Shape(Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0))
s2 = Shape(Point(0, 0.5), Point(0.5, 1), Point(1, 0.5), Point(0.5, 0))
print(s1 == s2)

s2 = Shape(Point(5, 5), Point(5, 6), Point(6, 6), Point(6, 5))
print(s1 < s2)

s3 = Shape(Point(10, 10), Point(10, 11), Point(11, 11), Point(11, 10))
shapes = [s3, s1, s2]
print(shapes)
print(sorted(shapes))
