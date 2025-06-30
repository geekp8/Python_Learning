#def main() with print and if __name__
#code level starts from level 0
def CalculatePercentage(Obtained,Total):#step3
   output=((Obtained/Total)*100) #business logic
   return output #step4


def main():
    print("Enter Total marks: ")
    value1=int(input())

    print("Enter obtained marks: ")
    value2=int(input())

    
    result=CalculatePercentage(Total=value1,Obtained=value2)#Keyword argument
    print("Percentage is: ",result)#step5


#starter
if __name__=="__main__" :   #line 1st of execution step1
    main() #call goes to main step2

#draw this in notebook
#int/int=float
# float*100=float    

