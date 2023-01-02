# Idea from: https://www.dataquest.io/blog/python-projects-for-beginners/
# Encrypts and Decrypts codes based on ASCII values 32-126
# Author: Andrew LeMay

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
    for i in range(len(codeList)):
        if i > 94:
            num = i-95
        else: num = i
        codeList[i] = int(ord(codeList[i])) + num
    codeList.reverse()
    for i in range(len(codeList)):
        if i > 94:
            num = i-95
        else: num = i
        codeList[i] += num
    for i in range(len(codeList)):
        if codeList[i] > 126:
            codeList[i] -= 95
        codeList[i] = chr(codeList[i])
    code = ""
    return code.join(codeList)

def decrypt(codeList):
    for i in range(len(codeList)):
        if i > 94:
            num = i-95
        else: num = i
        codeList[i] = int(ord(codeList[i]))-num
    codeList.reverse()
    for i in range(len(codeList)):
        if i > 94:
            num = i-95
        else: num = i
        codeList[i] -= num
    for i in range(len(codeList)):
        if codeList[i] < 32:
            codeList[i] += 95
        codeList[i] = chr(codeList[i])
    code = ""
    return code.join(codeList)

codeList = []
for letter in code:
    codeList.append(letter)

if process == 'e':
    print("Here is your code: " + encrypt(codeList))

else:
    print("Here is your decrypted message: " + decrypt(codeList))