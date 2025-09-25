# Password logic

#\/ This line is what the password is
validPassword = "PythonPass123"
#\/ This line is what the user inputs
userInput = input("Enter your password: ")
#\/ This loop checks if the password is correct, if they get it wrong it prints a message and asks them to try again and allows the user to input their password again.
while (validPassword != userInput):

    print("Incorrect password, try again.")

    userInput = input("Enter your password: ")
#\/ This line checks if the password is correct and prints a message if it is correct.
if userInput == validPassword:

    print("Access granted")
#\/ This line prints a message if the password is incorrect.
else:

    print("Access denied")