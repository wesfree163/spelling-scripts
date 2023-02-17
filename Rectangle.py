import math

class Rectangle:
    color = "red"

    def __init__(self, length = 1, width = 1):
        self.l = length
        slef.w = width

    def getArea(self):
        return math.pi * (self.r ** 2)

    def getPerimeter(self):
        return self.r * 2 * math.pi
    
    def printCircle(self):
        print("Circle with radius " + str(self.r) + " and color " + str(self.color))

c1 = Circle()
print(c1)
c1.printCircle()

c3 = Circle(7.14)
# c3.__init__(3)
c3.color = "Yellow"
c3.printCircle()
c3.unorthodoxName = "Godfrey"
print(f"""Area = {c3.getArea()}, it has an unorthodox name {c3.unorthodoxName}, and its color is {c3.color}, \n
        but be careful about making up .names on the fly without using the class definition""")

