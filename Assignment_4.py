#Collecting words from the user
verb1 = input ("Give me a verb:  ")
verb2 = input ("Give me another verb:  ")
noun1 = input ("Give me a noun:  ")
noun2 = input ("Give me another noun:  ")
adjective1 = input ("Give me an adjective:  ")
adjective2 = input ("Give me another adjective:  ")


userWords = [verb1, verb2, noun1, noun2, adjective1, adjective2]

text = "A luminous lantern let a tired traveler wander silently."

new_text = text.replace("luminous", userWords[4])
new_text = new_text.replace("lantern", userWords[2])
new_text = new_text.replace("let", userWords[0])
new_text = new_text.replace("tired", userWords[5])
new_text = new_text.replace("traveler", userWords[3])
new_text = new_text.replace("wander", userWords[1]) 

print (new_text)