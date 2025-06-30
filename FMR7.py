CheckEven=lambda no:no%2==0
Increase=lambda no:no+1
Sum=lambda A,B:A+B

#task is function
def filterX(Task,Values):
    Result=[]
    for no in Values:
        Ret=Task(no)
        if(Ret== True):
           Result.append(no)
    
    return Result  

def mapX(Task,Values):
    Result=[]

    for no in Values:
        Ret=Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task,Values):
    Result=0
    #[11,13,5,7,9,13,17]

    for no in Values:
        Result=Task(Result,no)
    #    Result.append(Result)

    return Result    


def main():

    Data=[7,10,15,12,4,6,9,8,12,16]
    print("Input data:",Data)

    FData=list(filterX(CheckEven,Data))#typecasting
    print("Filter Output:",FData)

    MData=list(mapX(Increase,FData))
    print("Map Output:",MData)

    RData=reduceX(Sum,MData)
    print("Reduce Output:",RData)

if __name__=="__main__":
    main()