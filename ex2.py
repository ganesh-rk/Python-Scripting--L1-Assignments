import sys

def isWhiteLine(arg1):
    if arg1.isspace() == False and arg1 =="":
        return True
    else:
        return(arg1.isspace())

def main():
    try:
        filename=sys.argv[1]
    except IndexError:
        print("Provide Argument")
        sys.exit()
    try:
        file=open(filename,"r")
    except (OSError, IOError):
        ##File does not exist, check name and location (add .txt if its a text document)
        sys.exit()
    for line in file:
        ls=line
        if(isWhiteLine(ls) is not True):
            print ls,
main()

