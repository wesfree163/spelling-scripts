import sys
import time
import os
import random
import numpy as np



def main():
    getValidScores()
    
    getLetGrades()
    
    return


def getLetGrades():
    
    aCount = 0
    bCount = 0
    cCount = 0
    dCount = 0
    fCount = 0
    score = 0
    
    for score in getValidScores():
        
        if 90 <= score <= 100:
            aCount += 1
        
        elif 80 <= score <= 89:
            bCount += 1
        elif 70 <= score <= 79:
            cCount += 1
        elif 60 <= score <= 69:
            dCount += 1
        elif score < 60:
            fCount += 1

    #recursive step gave recursion error, maximum recursion depth exceeded in comparison :( thinking about it wrong
    # while index <= getLetGrades().count:
    #    getLetGrades(index)
    #    index += 1

    time.sleep(1)
    print(f"You received {fCount} Fs")
    time.sleep(1)
    print(f"You received {dCount} Ds")
    time.sleep(1)
    print(f"You received {cCount} Cs")
    time.sleep(1)
    print(f"You received {bCount} Bs")
    time.sleep(1)
    print(f"You received {aCount} As")

    
def getValidScores():
    valid = False

    # The validator to see if scores are numeric and between 0 and 100
    while not valid:
        randnums = np.random.randint(1,100,5)
        response = input("Enter 5 test scores separated by spaces \n> ")

        # Checking that we entered all the correct things
        test_scores = response.split()
        if len(test_scores) != 5:
            print(f'Please enter 5 test scores, separated by spaces.')
            continue

         # Convert the strings into integers:
        try:
            for i in range(5):
                test_scores[i] = int(test_scores[i])
                valid = True
        except ValueError:
            print('Please enter the correct format of numbers, For example: {" ".join((str(i) for i in randnums))}')
            continue

        # Check that the numbers are between 1 and 69:    
        for i in range(5):
            if not (0 <= test_scores[i] <= 100):
                while not (0 <= test_scores[i] <= 100):
                    print('The numbers must all be between 0 and 100.')
                    print(f'Enter 5 test scores from 0 to 100, with spaces between')
                    print('each number. (For example: 5 17 23 42 50)')
                    response = input('> ')
                
                continue

    return test_scores


if __name__ == "__main__":
    main()
