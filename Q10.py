#Write a Python program to find the list of words that are longer than n from a given list of words.
lst=input("enter the list of words:")
lst2=[]
n=int(input("Enter length of the words you need:"))
for val in lst.split(","):
    if len(val)>n:
        lst2.append(val)
print(lst2)