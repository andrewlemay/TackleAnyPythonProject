# Idea from: https://www.dataquest.io/blog/python-projects-for-beginners/

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

codeList = []
for letter in code:
    codeList.append(letter)
print(codeList)

if process == 'e':
    print('e')

else:
    print('d')