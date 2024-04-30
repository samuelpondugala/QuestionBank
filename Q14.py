#Write a Python program to print the numbers of a specified list after removing even numbers from it
lst=[1,2,3,4,5,6,7]
for val in lst:
    if val%2==0:
        lst.remove(val)
print(lst)