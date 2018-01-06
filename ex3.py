import sys
class ValueError (Exception):
   """Raised when the input value is not of desired type"""
   

def isListOfInts(listin):
    try:
        if type(listin) is not list:
            raise ValueError
    except ValueError:
        print "ValueError: "+str(listin)+" arg not of <list> type"
        sys.exit()
    if len(listin)==0:
        return(True)
    else:
        i=0
        while(i<len(listin)):
            if type(listin[i]) is not int:
                return(False)
            i=i+1
        return(True)

def testList(arg):
    res=isListOfInts(arg)
    print arg ,"-->", res

def main():
    testList([1, 1.])

main()
