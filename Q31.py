#Write a Python program to count the number of elements in a list within a specified range.
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
min=int(input("Enter the minimum range:"))
max=int(input("Enter the maximum range:"))
count = 0
for element in numbers:
  if min <= element <= max:
    count += 1
print("The number of elements in the list within the range {},{} is:{}".format(min, max,count))