#Write a Python program to remove duplicates from a list
lst=['1','1','1','4','5']
lst1=[]
Set=set(lst)
for number in Set:
    lst1.append((number))
print(lst1)