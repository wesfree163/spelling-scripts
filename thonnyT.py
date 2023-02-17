class Shape:
    #class variable here
    def __init__(self):
        self.desc = "Shape"
        self.numSides = 0

    def toString(self):
        print("I am a " + self.desc
                + " with " + str(self.numSides)
                + " side(s).")

class Circle(Shape):
    def __init__(self, r=1):
        self.desc = "Circle"
        Circle.numSides = 1
        self.r = r
        
    def someMethod(self):
        super().toString()
        print(str(super().numSides))

s1 = Shape()
s1.toString()

c1 = Circle(3)
# c1.someMethod()
# print(f"Circle with number of sides {str(c1.r)}")
