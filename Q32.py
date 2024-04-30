#Write a Python program to check whether a list contains a sublist.
# Define a function to check if a list contains a sublist
def contains_sublist(list, sublist):
  # Loop through the list and check for the sublist starting from each index
  for i in range(len(list) - len(sublist) + 1):
    # If the sublist matches the slice of the list, return True
    if sublist == list[i:i + len(sublist)]:
      return True
  # If no match is found, return False
  return False

# Create a sample list and a sublist
list = [1, 2, 3, 4, 5, 6]
sublist = [3, 4, 5]

# Call the function and print the result
print(contains_sublist(list, sublist))
