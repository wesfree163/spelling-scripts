class Rectangle:

    def __init__(self, length = 1, width = 1):
        self.l = length
        self.w = width

    def getArea(self):
        val = int(str(self.l)) * int(str(self.w))
        print(f"Rectangle area = {str(val)}")
        return val

    def getPerimeter(self):
        val = int(str(self.l)) * 2 + int(str(self.w)) * 2
        print(f"Rectangle perimeter = {str(val)}")
        return val
    
    def printRectangle(self):
        print("Rectangle with length =  " + str(self.l) + " and width " + str(self.w))

r1 = Rectangle()
print(f"r1 Area")
r1.getArea()
print(f"r1 Perimeter")
r1.getPerimeter
r1.printRectangle()

r2 = Rectangle(2, 4)
print(f"r2 Area")
r2.getArea()
print(f"r2 Perimeter")
r2.getPerimeter
r2.printRectangle()

