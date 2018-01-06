def ruler(ran):
    v1=ran
    while(v1 > 0):
        l1=v1 % 10
        v1=v1/10
    i=1
    p1="                  "
    if ran >= 10:
        while(i<=l1):
            if i==1 and i!=l1:
                print p1+str(i),
            elif i <l1:
                print p1+str(i),
            else:
                print p1+str(i)
            i=i+1
    i=1
    while i <=ran:
        print i%10,
        i=i+1
ruler(51)    
