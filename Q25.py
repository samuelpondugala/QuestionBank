#Write a Python program to select an item randomly from a list.
import random

def select_random_item(input_list):
    if not input_list:
        return None  # Return None for an empty list
    else:
        return random.choice(input_list)

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_item = select_random_item(my_list)

if random_item is not None:
    print("Randomly selected item:", random_item)
else:
    print("The list is empty.")
