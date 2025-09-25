# Password logic

#\/ This line is what the password is

validPassword = "PythonPass123"

userInput = input("Enter your password: ")

while (validPassword != userInput):

    print("Incorrect password, try again.")

    userInput = input("Enter your password: ")

if userInput == validPassword:

    print("Access granted")

else:

    print("Access denied")