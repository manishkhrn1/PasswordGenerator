from random import randint



def NormalPassword(totalChar):
    password = ""
    for i in range(totalChar):
        randomSelector = randint(0,3)
        lowercase = randint(97,122)
        uppercase = randint(65,90)
        numbers = randint(48,57)

        if randomSelector == 0 or randomSelector == 1 :
            password += chr(lowercase)
        elif randomSelector == 2:
            password += chr(uppercase)
        elif randomSelector == 3:
            password += chr(numbers)
    print(password)
    
def SpecialPassword(totalChar):
    password = ""
    specialCharacter=['!','@','#','$','%','^','&','*']
    for i in range(totalChar):
        randomSelector = randint(0,4)
        lowercase = randint(97,122)
        uppercase = randint(65,90)
        numbers = randint(48,57)
        randomSpecial=randint(0,7)

        if randomSelector == 0 or randomSelector == 1:
            password += chr(lowercase)
        elif randomSelector == 2:
            password += chr(uppercase)
        elif randomSelector == 3:
            password += chr(numbers)
        elif randomSelector ==4:
            password += specialCharacter[randomSpecial]
    print(password)

totalChar= int(input("How long do you want your password to be ? : "))
prompt = input("Do you want a password with special character or normal one without special character, Enter n for normal , s for special character : ")
prompt = prompt.lower()
if (prompt=="s"):
    SpecialPassword(totalChar)
elif (prompt == "n"):
    NormalPassword(totalChar)