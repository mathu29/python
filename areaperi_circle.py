class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.radius*self.radius
    def perimeter(self):
        return 3.14*0.5*self.radius
crc=circle(4)
print("area",crc.area())
print("area",crc.perimeter())
