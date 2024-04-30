#Write a Python program to convert a list of characters into a string.
lst=[1,2,3,4,5,6]
lst1=[]
for val in lst:
    val=str(val)
    lst1.append(val)
print(lst1)