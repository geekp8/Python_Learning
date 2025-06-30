
#print("Inside main")
    #pass#keyword blank function

import sys

def main():
    print("No of command line arguments are:",len(sys.argv)) #name of the file 
    
    print("Data type of argv is:",type(sys.argv))#list modifiable ahe (mutable)
    print("First command line argument is:",sys.argv[0])
    print("First command line argument is:",sys.argv[1])
    print("First command line argument is:",sys.argv[2])
    print("First command line argument is:",sys.argv[3])
    #print("First command line argument is:",sys.argv[0])
if __name__=="__main__":
    main()
