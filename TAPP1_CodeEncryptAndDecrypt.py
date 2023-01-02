### Idea from: https://www.dataquest.io/blog/python-projects-for-beginners/
### Encrypts and Decrypts codes based on ASCII values 32-126
### Author: Andrew LeMay

# Cycles to only accept 'e' or 'd' as input
valid = True
while(valid):
    process = input('Type \'e\' to encrypt or \'d\' to decrypt:\n').lower()
    if process == 'e':
        code = input('Please enter what you would like to encrypt:\n')
        valid = False
    elif process == 'd':
        code = input('Please enter what you would like to decrypt:\n')
        valid = False
    else:
        print("Please only enter \'e\' for encrypt or \'d\' for decrypt")
        
def encrypt(codeList):
    # converts each character in the list to the corresponding ASCII value number and adds the index to that value
    for i in range(len(codeList)):
        # Prevents codes longer than 94 characters from breaking the code by escaping out of the intended ASCII values
        if i > 94:
            num = i-95
        else: num = i
        codeList[i] = int(ord(codeList[i])) + num
    # Reverses the list then adds the index to the value at that index
    codeList.reverse()
    for i in range(len(codeList)):
        # Prevents codes longer than 94 characters from breaking the code by escaping out of the intended ASCII values
        if i > 94:
            num = i-95
        else: num = i
        codeList[i] += num
    # Converts the ASCII values in the list to the corresponding character
    for i in range(len(codeList)):
        # Loops the ASCII value if it is outside of the intended range of values
        if codeList[i] > 126:
            codeList[i] -= 95
        codeList[i] = chr(codeList[i])
    code = ""
    # Returns a string version of the code list
    return code.join(codeList)

def decrypt(codeList):
    # converts each character in the list to the corresponding ASCII value number and subtracts the index from that value
    for i in range(len(codeList)):
        # Prevents codes longer than 94 characters from breaking the code by escaping out of the intended ASCII values
        if i > 94:
            num = i-95
        else: num = i
        codeList[i] = int(ord(codeList[i]))-num
    # Reverses the list then adds the index to the value at that index
    codeList.reverse()
    for i in range(len(codeList)):
        # Prevents codes longer than 94 characters from breaking the code by escaping out of the intended ASCII values
        if i > 94:
            num = i-95
        else: num = i
        codeList[i] -= num
    # Converts the ASCII values in the list to the corresponding character
    for i in range(len(codeList)):
        # Loops the ASCII value if it is outside of the intended range of values
        if codeList[i] < 32:
            codeList[i] += 95
        codeList[i] = chr(codeList[i])
    code = ""
    # Returns a string version of the code list
    return code.join(codeList)

# Creates a list version of the string that was provided through input
codeList = []
for letter in code:
    codeList.append(letter)

# Encrypts and prints the code if 'e' was input
if process == 'e':
    print("Here is your code: " + encrypt(codeList))

# Decrypts and prints the message if 'd' was input
else:
    print("Here is your decrypted message: " + decrypt(codeList))