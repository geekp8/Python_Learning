#def main() with print and if __name__
#code level starts from level 0
def CalculatePercentage(Obtained=400,Total=500):
   output=((Obtained/Total)*100) #business logic
   return output #step4


def main():
    
    result=CalculatePercentage(350,450)#these value will be final
    print("Percentage is: ",result)#step5

    result=CalculatePercentage(350)#350/500
    print("Percentage is: ",result)#step5

    result=CalculatePercentage()#uses default
    print("Percentage is: ",result)#step5


#starter
if __name__=="__main__" :   #line 1st of execution step1
    main() #call goes to main step2

#draw this in notebook
#int/int=float
# float*100=float    

