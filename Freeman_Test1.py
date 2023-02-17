def main():
    ### Strings
    fname = str(input("Enter your first name: "))
    lname = str(input("Enter your last name: "))
    print(f"{lname}, {fname}")
    print(f"{str(fname.lower())} {str(lname.upper())}")

    index = 0
    fname = fname[0:index] + "X" + fname[index+1: ]

    index = len(lname)-1
    lname = lname[0: index] + "Z" + lname [index+1: ]
    print(f"{fname} {lname}")

    ### Math
    a = int(input("Enter a number for 'a': "))
    b = int(input("Enter a number for 'b': "))
    
    def mathematics(a, b):
        result1 = (a + (b-7)/4)
        result2 = ((a ** 3) + (b ** 7))/((a+b)**.5)
        print(f"result1 = {result1: .3f}")
        print(f"result2 = {result2: .2f}")

        quotient = a//b
        remainder = a%b

        print("\nDivision:")
        print(f"Quotient = {quotient}")
        print(f"Remainder = {remainder}")
    mathematics(a, b)

    def looping():
        given1 = int(input("Enter two numbers between 32 and 126:\n"))
        given2 = int(input())
        while (given1 > 126 or given1 < 32) and (given2 > 126 or given2 < 32):
            print("Integer(s) out of range\n")
            given1 = int(input("Enter two numbers between 32 and 126:\n"))
            given2 = int(input())


        if given1 > given2:
            greater = given1
            lesser = given2
        else:
            greater = given2
            lesser = given1
            
        while lesser < greater+1:
            print(f"{lesser}: {chr(lesser)}")
            lesser += 1
    looping()

    string = str(input("Enter a line of text:\n"))
    def palindrome(string, boolean = False):
        if string == string[::-1]:
            print(f"String reversed is equal: {string} - {string[::-1]}")
            boolean = True
            return boolean
        else:
            print(f"String reversed is not equal: {string} - {string[::-1]}")
            return boolean
    palindrome(string, )

if __name__ == "__main__":
    main()
