# Write a program that:
# 1.Asks the user to enter a sentence (for example: “Python is awesome!”).
# 2.Displays the length of the entered string.
# 3.Removes spaces at the ends and displays the length again.
# 4.Replaces all occurrences of the word “awesome” with “fun” and displays the result.
# 5.Adds another word “Indeed!” to the end of the string, separated by a space.
# 6.Prints the final string and its length.

# first try

sentence = input("Enter a sentence: ")
print("1)" + sentence)
print("2)" , (len(sentence)))
print("3)" , len(sentence.strip()))  
modified = sentence.replace("awesome", "fun")
print("4)" + modified)
final = modified + "Indeed!"
print("5)" , final)
print("6)" , final , len(final))

# second try

sentence = input("Enter a sentence: ")
print(f"1) {sentence}")
print(f"2) {len(sentence)}")
trimmed = sentence.strip()
print(f"3) {len(trimmed)}")
modified = trimmed.replace("awesome", "fun")
print(f"4) {modified}")
final = modified + "Indeed!"
print(f"5,6) {final} {len(final)}")



