def Increase(A):
    return A+1

def Demo(Task,Value):
    Result=[]

    for no in Value:
        #print(Task(no))
        ret=Task(no)
        Result.append(ret)

    return Result   

Data=[13,17,10,14,11]    

RData=list(Demo(Increase,Data))
#Demo(Increase,Data)
print(RData)