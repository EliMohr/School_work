#Collecting words from the user
print("You will be asked to provide some words to fill in the blanks of a story.")
print("Here is an example of the story:")
print("Together, the fox and river learned that when they run and dance, even small steps feel brave.")
#txtFile = open("UserWords.txt", "r")
#txtFile = open("UserWords.txt", "w")

verb1 = input ("Give me a verb:  ")
#txtFile.write(verb1 + "\n")
#txtFile.close()
verb2 = input ("Give me another verb:  ")
#txtFile.write(verb2 + "\n")
#txtFile.close()
noun1 = input ("Give me a noun:  ")
#txtFile.write(noun1 + "\n")
#txtFile.close()
noun2 = input ("Give me another noun:  ")
#txtFile.write(noun2 + "\n")
#txtFile.close()
adjective1 = input ("Give me an adjective:  ")
#txtFile.write(adjective1 + "\n")
#txtFile.close()
adjective2 = input ("Give me another adjective:  ")
#txtFile.write(adjective2 + "\n")
#txtFile.close()


userWords = [verb1, verb2, noun1, noun2, adjective1, adjective2]
#txtFile.write(str(userWords))
text = "Together, the fox and river learned that when they run and dance, even small steps feel brave."

new_text = text.replace("fox", userWords[0])
new_text = new_text.replace("river", userWords[1])
new_text = new_text.replace("run", userWords[2])
new_text = new_text.replace("dance", userWords[3])
new_text = new_text.replace("small", userWords[4])
new_text = new_text.replace("brave", userWords[5])
print (new_text)
#get the old words from the last time the user used our adlib app
print("Here were the words you used last time:")
with open("UserWords.txt", "r") as txtFile:
    lines = txtFile.readlines()

lines = [line.strip() for line in lines]

for line in lines:
    print(line.strip())
#save the new words for next time
txtFile = open("UserWords.txt", "w")
txtFile.write(verb1 + "\n")
txtFile.write(verb2 + "\n")
txtFile.write(noun1 + "\n")
txtFile.write(noun2 + "\n")
txtFile.write(adjective1 + "\n")
txtFile.write(adjective2 + "\n")
txtFile.close() 
