import sys
import time
import os
import random
import numpy as np



def main():
    # getValidScores()
    
    getLetGrades()
    
    return


def getLetGrades(index = 0):

    if index == 5:
        return
    
    aCount = 0
    bCount = 0
    cCount = 0
    dCount = 0
    fCount = 0
    score = 0
    
    
    if 90 <= getValidScores()[index] <= 100:
        aCount += 1
    elif 80 <= getValidScores()[index] <= 89:
        bCount += 1
    elif 70 <= getValidScores()[index] <= 79:
        cCount += 1
    elif 60 <= getValidScores()[index] <= 69:
        dCount += 1
    elif getValidScores()[index] < 60:
        fCount += 1

    #recursinve 
    while index <= getLetGrades().count:
        getLetGrades()
        index += 1
        


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
