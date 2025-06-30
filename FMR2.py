from functools import reduce

# def CheckEven(no):
#     return no%2==0

CheckEven=lambda no:no%2==0

# def Increase(no):
#     return no+1
Increase=lambda no:no+1

# def Sum(A,B):
#     return A+B

Sum=lambda A,B:A+B

Data=[7,10,15,12,4,6,9,8,12,16]
print("Input data:",Data)

FData=list(filter(CheckEven,Data))#typecasting
print("Filter Output:",FData)

MData=list(map(Increase,FData))
print("Map Output:",MData)

RData=reduce(Sum,MData)
print("Reduce Output:",RData)