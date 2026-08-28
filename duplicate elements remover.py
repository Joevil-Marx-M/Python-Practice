l1=eval(input("enter list"))
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        pass
print("original list",l2)
