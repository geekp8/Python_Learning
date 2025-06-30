
#print("Inside main")
    #pass#keyword blank function

import sys

def main():
    print("No of command line arguments are:",len(sys.argv)) #name of the file 
    print("List of commandline arguments are: ")
    
    # for i in len(sys.argv) :
    #     print("Total no of arguments are:",len(sys.argv))
    #     i=i+1
    
    #use with for
    i=1
    while(i<(len(sys.argv))):
        print(sys.argv[i])
        i=i+1
    # for value in sys.argv:
    #     print("total arguments:",value)
    
if __name__=="__main__":
    main()
