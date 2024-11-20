class shape:
    def __init__(self,length,width,sides):
        self.length=length
        self.width=width
        self.sides=sides
    def area(self):
        self.Area=self.length*self.width
    def perimeter(self):
        self.Perimeter=(self.width*self.sides)+(self.length*self.Area)
class circle(shape):
    def __init__(self,width,):
        super().__init__(width)

    def area(self):
        self.radius=self.width/2
        self.Area=self.radius**2*3.14
    def perimeter(self):
        self.Perimeter=self.width*3.14

class square(shape):
    def __init__(self,width,length):
        super().__init__(width,length)
        

