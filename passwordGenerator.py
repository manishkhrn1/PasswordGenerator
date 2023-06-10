from random import randint

password = ""

for i in range(12):
    randomSelector = randint(0,2)
    lowercase = randint(97,122)
    uppercase = randint(65,90)
    numbers = randint(48,57)

    if randomSelector == 0 :
        password += chr(lowercase)
    elif randomSelector == 1:
        password += chr(uppercase)
    elif randomSelector == 2:
        password += chr(numbers)
print(password)
    