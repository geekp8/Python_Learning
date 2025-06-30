import sys


def Add(value1,value2):
    Ans=0
    Ans=value1+value2
    return Ans


def main():
    # value1=int(input("Enter first number:"))#in one line
    # value2=int(input("Enter second number:"))
    #command line argumets

      if(len(sys.argv)==2):
           if(sys.argv[1]=="--h"):
           print("This application is used to perform addition of 2 numbers")
           return
      
           if(len(sys.argv[1]=="--u")):
           print("Execute the code as :")
           return

           if(len(sys.argv )!=3):
           print("Insufficients no of arguments")
           print("you can use --h for help and --u as usage")
           return

      no1=int(sys.argv[1])
      no2=int(sys.argv[2])

      Result=Add(no1,no2)

      print("Addition is",Result)    


if __name__=="__main__":
    main()    
