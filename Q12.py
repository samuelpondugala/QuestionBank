#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
lst=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
lst.remove(lst[0])
lst.remove(lst[3])
lst.remove(lst[3])
print(lst)
