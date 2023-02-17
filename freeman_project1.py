
# Function to get keyboard input, nested in a later function
def getInput():
    arrayString = list(input("Enter a line to encrypt: \n"))
    return arrayString

def decInput():
    arrayString = list(input("Enter a line to decrypt: \n"))
    return arrayString

# Main encrypting function, using another function
def doEncryption(n): # parameter can be of type Int
    someText = getInput()
    newText = ""
    indexC = ""

    n = int(input("Numeric encryption key (positive or negative whole number): "))
    # finding one character at a time and then setting the alphabet's numeric index at that character
    
    for char in someText:
       indexC = char
       i = ord(indexC)
       i += n
       if i > 126:
           i -= 95
       newText += chr(i) # a new text will be generated
    
    return newText

def doDecryption(n, line):
    someText = line
    newText = ""
    indexC = ""
    
    # finding one character at a time and then setting the alphabet's numeric index at that character
    for char in someText:
       indexC = char
       i = ord(indexC)
       i -= n
       if i < 32:
           i += 95
       newText += chr(i) # a new text will be generated
    return newText

def crack(n, line):
    if n > 0:
        print(f"{doDecryption(n, line)}\n")
        crack(n-1, line)
    
booleanFlag = True
while booleanFlag:
    toggle = str(input("(E)ncryption, (D)ecryption, (C)rack, or e(X)it? \n"))
    if toggle == 'e' or toggle == 'E':
        print(f"{doEncryption(0)}\n")
        booleanFlag = True
    elif toggle == 'd' or toggle == 'D':
        line = decInput()
        n = int(input(f"""Encryption key?"""))
        print(f"{doDecryption(n, line)}")
        print("\n")
        booleanFlag = True
    elif toggle == 'c' or toggle == 'C':
        line = decInput()
        crack(126, line)
        booleanFlag = True
    elif toggle == 'x' or toggle == 'X':
        booleanFlag = False
        exit()