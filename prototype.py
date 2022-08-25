import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        new_start = Point(self.start.x, self.start.y)
        new_end = Point(self.end.x, self.end.y)
        return Line(new_start, new_end)

start_point = Point(5,6)
end_point = Point(5,6)
line1 =Line(start_point,end_point)
line2= line1.deep_copy()

print(line1)
print(line2)

