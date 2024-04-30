#Write a Python program to generate and print a list of first and last 5 elements where the values are
# square of numbers between 1 and 30 (both included).
lst=[]
for val in range(1,31):
    number=val**2
    lst.append(number)
print("List of fist five numbers:{}".format(lst[0:6]))
print(("List of Last five numebrs:{}".format(lst[:-6:-1])))