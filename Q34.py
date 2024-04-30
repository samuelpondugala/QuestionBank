#Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
#Sample list : ['p', 'q']
#n =5
#Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
lst=['p','q']
lst1=[]
n=int(input("Enter number for a range:"))
if n<=0:

    print("please enter valid number!!")
else:
    for i in range(1,n+1):
        for value in lst:
            number=value+str(i)
            lst1.append(number)
print(lst1)