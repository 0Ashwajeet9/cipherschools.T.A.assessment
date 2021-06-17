for i in range(0,int(input())):
    s1=input()
    s2=input()
    list1=list(s1)
    list3=list1
    list2=list(s2)
    list1.sort()
    for i in list1:
        if i in list2:
            list3.remove(i)
    p=list2[0]
    list3.sort()
    for i in list3:
        if ord(i)<=ord(p):
            d=d+i
        else:
            s=s+i    
    print(d+s2+s)
