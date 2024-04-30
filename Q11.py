#Write a Python function that takes two lists and returns True if they have at least one common member
lst1=["sam","dav","python","java"]
lst2=["sam","david","Samuel","Java"]
lst3=[]
for v in lst1:
    for k in lst2:
        if v==k:
            lst3.append(v)
if len(lst3)>0:
    print("words that are same in 1st and 2nd lists are:{}".format(lst3))
else:
    print("There are no common words between lists!!")