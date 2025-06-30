def Add(value1,value2):
    Ans=0
    Ans=value1+value2
    return Ans


def main():
    value1=int(input("Enter first number:"))#in one line
    value2=int(input("Enter second number:"))

    Result=Add(value1,value2)

    print("Addition is",Result)    


if __name__=="__main__":
    main()    
