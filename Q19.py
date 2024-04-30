#Write a Python program to get the difference between the two lists.
def list_difference(list1, list2):
    # Using list comprehension to find the difference
    difference = [item for item in list1 if item not in list2]

    return difference

# Example usage
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

result = list_difference(list_a, list_b)
print("Difference between list_a and list_b:", result)
