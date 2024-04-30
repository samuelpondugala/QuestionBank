#Write a Python program to generate all sublists of a list.
lst=[1,2,3,4]
sublist=[]
for value in range(len(lst)):
    for number in range(value+1,len(lst)+1):
        sublist.append(lst[value:number])
print(sublist)