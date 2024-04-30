#Write a Python program to generate all permutations of a list in Python.
def generate_permutations(lst, start=0):
    if start == len(lst) - 1:
        yield lst.copy()
    else:
        for i in range(start, len(lst)):
            # Swap the current element with the element at index 'start'
            lst[start], lst[i] = lst[i], lst[start]

            # Recursively generate permutations for the remaining elements
            yield from generate_permutations(lst, start + 1)

            # Swap back to the original order for backtracking
            lst[start], lst[i] = lst[i], lst[start]


# Example usage
my_list = [1, 2, 3]
all_permutations = list(generate_permutations(my_list))

# Print the result
for permutation in all_permutations:
    print(permutation)
