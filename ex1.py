def ruler(ran):
    v1=ran
    while(v1 > 0):
        l1=v1 % 10
        v1=v1/10

    #first digit of the input will be stored in l1 now
    
    i=1
    p1="                  "
    if ran >= 10:
        while(i<=l1): # printing the top row values
            if i==1 and i!=l1:
                print p1+str(i),
            elif i <l1:
                print p1+str(i),
            else:
                print p1+str(i)
            i=i+1
    i=1
    while i <=ran: # printing the bottom row values
        print i%10,
        i=i+1

def main():
    ruler(43)    
    #ruler(5)
    #ruler(10)
    #ruler(25)
    #ruler(51)
    #ruler(80)

main()
