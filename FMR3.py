from functools import reduce


# CheckEven=lambda no:no%2==0
# Increase=lambda no:no+1
#Sum=lambda A,B:A+B

Data=[7,10,15,12,4,6,9,8,12,16]
print("Input data:",Data)

FData=list(filter(lambda no:no%2==0,Data))#typecasting
print("Filter Output:",FData)

MData=list(map(lambda no:no+1,FData))
print("Map Output:",MData)

RData=reduce(lambda A,B:A+B,MData)
print("Reduce Output:",RData)