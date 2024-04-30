#Write a python program to check whether two lists are circularly identical.
def are_circularly_identical(list1, list2):
    if len(list1) != len(list2):
        return False

    # Concatenate the first list with itself
    concatenated_list = list1 + list1

    # Check if the second list is a sublist of the concatenated list
    return all(item in concatenated_list for item in list2)

# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 1, 2, 3]

if are_circularly_identical(list_a, list_b):
    print("The lists are circularly identical.")
else:
    print("The lists are not circularly identical.")
