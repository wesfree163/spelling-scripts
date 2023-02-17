import turtle
import random

turtwig = turtle.Turtle()
# turtwig square
def square(sLength):
    for i in range(4):
        turtwig.forward(sLength)
        # print(turtwig)
        turtwig.right(-90)
        # print(turtwig)

def pentagram(sLength):
    for i in range(5):
        turtwig.forward(sLength)
        # print(turtwig)
        turtwig.right(-144)
        # print(turtwig)

def polygon(sLength, sCount):
    turtwig.right(108)
    for i in range(sCount):
        turtwig.forward(-sLength)
        # print(turtwig)
        turtwig.right(int(360/sCount))
        # print(turtwig)

def circle(sLength):
    turtwig.right(90)
    for i in range(360):
        turtwig.forward(sLength)
        # print(turtwig)
        turtwig.right(-1)
        # print(turtwig)

def spiral(sLength):
    turtwig.right(90)
    for i in range(100):
        bend = 0.0
        turtwig.forward(5 - i)
        # print(turtwig)
        turtwig.right(15)
        # print(turtwig)

def bellPentagram(sLength):
    for i in range(5):
        circle(0.5)
        circle(0.4)
        circle(0.3)
        circle(0.2)
        circle(0.1)
        turtwig.forward(-sLength)
        # print(turtwig)
        turtwig.right(-144)
        # print(turtwig)

def abstractShape(sLength, sCount):
    sLength = random.randrange(150, 270)
    sCount = random.randrange(3, 12)
    for i in range(sCount):
        circle(0.4)
        circle(0.3)
        circle(0.2)
        turtwig.forward(sLength)
        # print(turtwig)
        turtwig.right((-4/3) * (int(360/sCount)))
        # print(turtwig)

def multiPentagram(sLength):
    for i in range(5):
        for i in range(5):

                # times 100 traces 
            for i in range(5):
                for i in range(5):
                    turtwig.forward(sLength/100)
                    # print(turtwig)
                    turtwig.right(-144)
                    # print(turtwig)


            turtwig.forward(sLength/10)
            # print(turtwig)
            turtwig.right(-144)
            # print(turtwig)
        turtwig.forward(sLength)
        # print(turtwig)
        turtwig.right(-144)
        # print(turtwig)


# lInput = int(input("Enter a number for the lenth of sides"))
# square(lInput)

# pentagram(270)

# polygon(300, 3)

# circle(1)

# bellPentagram(270)

rand = random.randrange(150, 510)
def margatneP(rand):
    # rand = random.randrange(150, 510)
    # rand = random.randrange(150, 510)
    multiPentagram(rand)
    # circle(random.randrange(3,6))

    polygon(rand * (0.618), 5)
    margatneP(rand)
margatneP(rand)

# unfinished kingdom heart
# polygon(100, 1)
# turtwig.right(180)
# turtwig.right(1)

# spiral(1)

# abstractShape(0, 0)
turtle.mainloop()