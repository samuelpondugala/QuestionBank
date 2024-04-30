#Write a Python program to find common items from two lists.
n=(input("Enter the numbers for first list:"))
i=(input("Enter the numbers for second list:"))
lst1=[]
lst2=[]
for value1 in n.split(","):
    lst1.append(value1)
for value2 in i.split(","):
    lst2.append(value2)
common_list=[]
for number in lst1:
    for number1 in lst2:
        if number==number1:
            common_list.append(number1)
print("The common items in both the lists are:",common_list)
#====================OR========================
list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9]
set1 = set(list1)
set2 = set(list2)
common_items = set1.intersection(set2)
common_list = list(common_items)
print(common_list)
