#Eli Mohr Assignment 3
#\/this imports the time module so we can pause the program.
import time
import os
#\/this is saying what the password is.
#validPassword = "JimmyJohns123"

#encrypts the password
def passwordEncrypt(password):
    import string
    alphabet = string.ascii_lowercase + " "
    alphabetList = []
    for character in alphabet:
        alphabetList.append(character)
    print(password.replace(alphabetList[1], alphabetList[26]))
#\/this is asking the user to input a new password.        
NewPassword = input("Enter a new password: ")
validPassword = NewPassword
passwordEncrypt(validPassword)


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
