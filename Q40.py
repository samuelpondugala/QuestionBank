#Write a Python program to split a list based on first character of word.
# Import the groupby function from the itertools module
from itertools import groupby

# Define a list of words
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think', 'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

# Use the groupby function to group the words by their first letter
# The key function is a lambda expression that returns the first character of each word
groups = groupby(word_list, key=lambda x: x[0])

# Loop through the groups and print the first letter and the words starting with that letter
for letter, words in groups:
  print(letter)
  for word in words:
    print(word)
  print()

