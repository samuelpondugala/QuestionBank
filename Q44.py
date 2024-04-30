#Write a Python program to generate groups of five consecutive numbers in alist
# Define a function to generate groups of five consecutive numbers in a list
def groups_of_five(lst):
  # Use list comprehension to create a new list of lists with five consecutive numbers
  return [lst[i:i + 5] for i in range(0, len(lst), 5)]

# Create a sample list of numbers
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the function and print the result
print(groups_of_five(sample_list))
