#Write a Python program to change the position of every n-th value with the (n+1)th in a list.
#Sample list: [0,1,2,3,4,5]
#Expected Output: [1, 0, 3, 2, 5, 4]
def change_pos(lst):
  # Loop through the list with a step of 2
  for i in range(0, len(lst) - 1, 2):
    # Swap the elements at the current index and the next index
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
  # Return the modified list
  return lst

# Create a sample list
sample_list = [0, 1, 2, 3, 4, 5]
# Change the position of every n-th value with the (n+1)th
result = change_pos(sample_list)
# Print the result
print(result)
