#frequency of all elements in the list without using dict
l1=eval(input("enter list"))
l2=[]
for i in l1:
    if i in l1:
        l2.append(i)
    else:
        pass
for j in l2:
    a=l1.count(j)
    print("No of occurences of",j,"is",a,"times")
