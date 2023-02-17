import random

name = input("What's your name? \n")
points = 0
qCount = 0
score = 0.0
ans = 0

while qCount < 10:
    rand1 = random.randrange(1, 100)
    rand2 = random.randrange(1, 100)
    guess = int(input(f"What is {rand1} + {rand2}? \n"))
    ans = rand1 + rand2
    if guess < ans:
        print(f"Good try, but you're a little low. The answer was {ans}")
    elif guess == ans:
        print("Good job!")
        points += 1
    elif guess > ans:
        print(f"Good try, but you're a little high. The answer was {ans}")
    qCount += 1
score = 100 * (points/qCount)

print(f"Thanks for playing, {name}, your score was {score}%.")