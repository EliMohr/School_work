#Collecting words from the user
txtFile = open("UserWords.txt", "w")

verb1 = input ("Give me a verb:  ")
txtFile.write(verb1 + "\n")
#txtFile.close()
verb2 = input ("Give me another verb:  ")
txtFile.write(verb2 + "\n")
#txtFile.close()
noun1 = input ("Give me a noun:  ")
txtFile.write(noun1 + "\n")
#txtFile.close()
noun2 = input ("Give me another noun:  ")
txtFile.write(noun2 + "\n")
#txtFile.close()
adjective1 = input ("Give me an adjective:  ")
txtFile.write(adjective1 + "\n")
#txtFile.close()
adjective2 = input ("Give me another adjective:  ")
txtFile.write(adjective2 + "\n")
txtFile.close()


userWords = [verb1, verb2, noun1, noun2, adjective1, adjective2]
#txtFile.write(str(userWords))
text = "A luminous lantern let a tired traveler wander silently."

new_text = text.replace("luminous", userWords[4])
new_text = new_text.replace("lantern", userWords[2])
new_text = new_text.replace("let", userWords[0])
new_text = new_text.replace("tired", userWords[5])
new_text = new_text.replace("traveler", userWords[3])
new_text = new_text.replace("wander", userWords[1]) 
print (new_text)

#get the old words from the last time the user used our adlib app
with open("UserWords.txt", "r") as txtFile:
    lines = txtFile.readlines()
    
for line in lines:
    print(line)

#Insert our old words into the adlib
print("Here is the old story without your new words:")
print(text)