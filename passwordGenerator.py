from random import randint

#If the user prefers a password without any special characters
def NormalPassword(totalChar):
    password = ""
    for i in range(totalChar):
        randomSelector = randint(0,3)  #This randomly chooses the next character
        lowercase = randint(97,122)    #This will randomly choose an ASCII code for lowercase letters
        uppercase = randint(65,90)      #This will randomly choose an ASCII code for uppercase letters
        numbers = randint(48,57)        #This will randomly choose an ASCII code for numbers

        # here user gets more chances of getting a lowercase letters than the other characters
        if randomSelector == 0 or randomSelector == 1 :
            password += chr(lowercase)
        elif randomSelector == 2:
            password += chr(uppercase)
        elif randomSelector == 3:
            password += chr(numbers)
    print(password)

#If the user wants a password with some special characters  
def SpecialPassword(totalChar):
    password = ""
    specialCharacter=['!','@','#','$','%','^','&','*']
    for i in range(totalChar):
        randomSelector = randint(0,4)
        lowercase = randint(97,122)   #This will randomly choose an ASCII code for lowercase letters
        uppercase = randint(65,90)    #This will randomly choose an ASCII code for uppercase letters
        numbers = randint(48,57)       #This will randomly choose an ASCII code for numbers
        randomSpecial=randint(0,7)     #This will randomly choose a special character

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
prompt = prompt.lower()         #This will convert the input of the user into lowercase
if (prompt=="s"):                  #If user chooses 's' then it goes to special character else normal
    SpecialPassword(totalChar)      
elif (prompt == "n"):
    NormalPassword(totalChar)