#Eli Mohr Assignment 3
#\/this imports the time module so we can pause the program.
import time
import os
#\/this is saying what the password is.
#validPassword = "JimmyJohns123"

#encrypts the password
def passwordEncrypt(password):
    import string
    alphabet = string.ascii_lowercase + " " + string.ascii_uppercase
    number = string.digits
    alphabetList = []
    for character in number:
        alphabetList.append(character)
    for character in alphabet:
        alphabetList.append(character)
        #\/ this stuff down here is made by AI
    # number[1] is '1' and number[9] is '9' (digits string is '0123456789')
    # build a lowercase-only list so 'first letter' means index 0 -> 'a'
    lowercase = list(string.ascii_lowercase)  # ['a','b',...,'z']
    # lowercase[0] is the first letter 'a', lowercase[20] is the 21st letter 'u'
    # replace digit '1' with '9' and first lowercase letter with the 21st lowercase
    
    #\/ now this is me
    uppercase = list(string.ascii_uppercase)
    return password.replace(number[1], number[9]).replace(lowercase[0], lowercase[20]).replace(uppercase[0], uppercase[20])
    #return (password.replace(alphabetList[1], alphabetList[21]))
    
    #/\ AI did that I did add the uppercase part though 

newPassword = input("Enter a new password: ")
validPassword = newPassword
encryptedPassword = passwordEncrypt(validPassword)
print(encryptedPassword)


#\/this is how many chances the user has before the countdown starts.
maxTries = 6
#\/this is how many seconds to count down once the user runs out of tries.
countdownSeconds = 3
#\/this is asking the user to input their password.
enteredPassword = input("Enter your password: ")
#\/this is setting a counter for how many times the user has tried to enter the password.
tryCount = 0
#\/this is a while loop that will keep asking the user to enter their password until they enter the correct one or exceed the number of tries.
while (validPassword != enteredPassword):
    print("Incorrect password, try again.")
    enteredPassword = input("Enter your password: ")
    tryCount += 1
    if tryCount >= maxTries:
        print("Too many failed attempts.")
        #\/this counts down before closing the program.
        for secondsLeft in range(countdownSeconds, 0, -1):
            print(f"Locked for {secondsLeft} seconds...")
            time.sleep(1)
        print("Access denied")
        tryCount = 1
#\/this is checking if the user has entered the correct password.
if enteredPassword == validPassword:
    print("Access granted")
#\/this is saying that if the user has not entered the correct password, access is denied.
else:
    print("Access denied")  
