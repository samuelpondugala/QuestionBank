#Write a Python program to find missing and additional values in two lists.
#Sample data : Missing values in second list: b,a,c
#Additional values in second list: g,h
# Define two sample lists
list1 = ['a', 'b', 'c', 'd', 'e','f']
list2 = ['d', 'e', 'f', 'g', 'h']
# Convert the lists to sets
set1 = set(list1)
set2 = set(list2)
# Find the missing values in list2 by subtracting set2 from set1
missing_values = set1 - set2
# Find the additional values in list2 by subtracting set1 from set2
additional_values = set2 - set1
# Print the missing and additional values in list2
print("Missing values in second list:", missing_values)
print("Additional values in second list:", additional_values)
