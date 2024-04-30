#Write a Python program to flatten a shallow list.
lst=[[1,2,3],[4,5,6]]
lst1=[]
for num in lst:
    for val in num:
        lst1.append(val)
print(lst1)