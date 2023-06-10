from random import randint



def NormalPassword():
    password = ""
    for i in range():
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
    

    NormalPassword()