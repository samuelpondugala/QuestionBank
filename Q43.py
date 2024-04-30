#Write a Python program to split a list into different variables.
list=['a','b','c','d','e','f','g']
a=[]
b=[]
c=len(list)
for value in range(c-3):
    a.append(list[value])
for value in range(4,c):
    b.append(list[value])
print("First split=",a)
print("second split=",b)