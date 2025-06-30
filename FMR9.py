

CheckEven=lambda no:no%2==0
Increase=lambda no:no+1
Sum=lambda A,B:A+B

from MarvellousFMR import filterX,mapX,reduceX

def main():

    Data=[]
    print("enter no of elements: ")
    size=int(input())

    print("Please eneter numeric value")

    for i in range(size):
        no=int(input())
        Data.append(no)

        
        
    print("Input data:",Data)

    FData=list(filterX(CheckEven,Data))#typecasting
    print("Filter Output:",FData)

    MData=list(mapX(Increase,FData))
    print("Map Output:",MData)

    RData=reduceX(Sum,MData)
    print("Reduce Output:",RData)

if __name__=="__main__":
    main()