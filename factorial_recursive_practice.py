import time

def factorial(n):
    print(f"Calculating {n}!...")
    if n == 1 or n == 0:
        print(f"Done calculating {n}! Returning 1")
        time.sleep(1)
        return 1

    time.sleep(1)
    answer = n * factorial(n-1)
    print(f"Done calculating {n}! Returning {answer}")
    time.sleep(1)
    return answer

def main():
    fini = False
    while not fini:
        try:
            num = int(input("Enter n to calculate n!: "))
            fini = True
        except ValueError:
            print("You need to enter an integer")

    print(f"{num}! = {factorial(num)}")

if __name__ == "__main__":
    main()
