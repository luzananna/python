#Task: “Word Mixer”

# Objective:
# Write a program that:
# 1) Asks the user to enter a sentence.
# 2) Splits it into words.
# 3) Counts the number of words.
# 4) Reverses the order of the words (last → first).
# 5) Joins them back into a string (separated by spaces).
# 6) Outputs:
# • the original sentence,
# • the list of words,
# • the number of words,
# • the reversed sentence.


sentence = input("Enter a sentence: ")
words = sentence.split()
print(words)
count = len(words)
reversed = words[::-1]
print(reversed)
reversed_sentence = " ".join(reversed)
print(reversed_sentence)

print("\nOriginal sentence:", sentence)
print("Words:", words)
print("Word count:", count)
print("Reversed sentence:", reversed_sentence)