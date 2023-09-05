#Exercise 4: String Manipulation - Reverse a String
#Reverse a string using a loop. This is a common exercise that has applications in text processing.


text = "Python"
final_text = ""

for letter in text:
    final_text = letter + final_text

print("Reversed text:", final_text)
