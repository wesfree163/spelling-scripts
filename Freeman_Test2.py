
# Part A: creating a dog class and methods
class Dog:
    # name = "dogName"
    
    def __init__(self, name):
        self.description = "dog"
        self.name = name

    def getName():
        return self.name

    def speak():
        print("woof woof!")

# Part B: creating a smallDog class to inherit from original Dog class
class SmallDog:
    def __init__(self, name):
        self.description = "small dog"
        self.name = name

    def getName():
        return self.name

    def speak():
        print("yip yip!")

def main():
    d1 = Dog("Barney")
    d2 = SmallDog("Rocket")

if __name__ == "__main__":
    main()
