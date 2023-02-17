# import random
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import colors
# from matplotlib.ticker import PercentFormatter

# Create a random number generator with a fixed seed for reproductibility
# rng = np.randome.default_rng(19680801)




howManyRolls = int(input("Enter how many total rolls: \n"))
howManyDice = int(input("Enter how many dice to roll: \n"))
### How many rolls can be a parameter ###
#   How many dice can be a second parameter
#   Run a while/for loop based on the number of rolls integer
#   Have a small dice method already, adjust to accomodate number of dice integer
#   Record the sum of each dice roll in a list structure
#   Last plot the results as a HISTOGRAM
### EZ ###



diOne = 1
diTwo = 1


def dice():
    diOne = random.randrange(1, 7) # randint(inclusiveInt, inclusiveInt)
    diTwo = random.randrange(1, 7)
    print(f"Roll One: {diOne}")
    print(f"Roll Two: {diTwo}\n")
    if diOne == 1 and diTwo == 1:
            print("You rolled Snake Eyes! \nYou Lose")
            exit(0)
    while(True):
        dice()
        diOne = random.randrange(1, 7)
        diTwo = random.randrange(1, 7)
        
dice()
