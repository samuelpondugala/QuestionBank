#Write a Python program to create multiple lists.
n=int(input("Enter how many lists you want to create:"))
lists=[]
for i in range(n+1):
    lists.append([])
print(lists)
