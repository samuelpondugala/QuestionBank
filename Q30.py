#Write a Python program to get the frequency of the elements in a list.
def get_element_frequency(input_list):
    frequency_dict = {}

    for element in input_list:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    return frequency_dict

# Example usage:
my_list = [1, 2, 3, 1, 2, 4, 5, 1, 2, 2]
frequency_result = get_element_frequency(my_list)

print("Element frequencies:")
for element, frequency in frequency_result.items():
    print(f"{element}: {frequency}")

