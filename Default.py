#def main() with print and if __name__
#code level starts from level 0
def CalculatePercentage(Obtained,Total=500):#step3 #default if type/value not given it will take default both of the params can be default, but if multiple,
    # use default at the end
   output=((Obtained/Total)*100) #business logic
   return output #step4


def main():
    # print("Enter Total marks: ")
    # value1=int(input())
    #remove above lines 
    print("Enter obtained marks: ")
    value2=int(input())

    
    result=CalculatePercentage(value2)#passing single as value is set for default
    print("Percentage is: ",result)#step5


#starter
if __name__=="__main__" :   #line 1st of execution step1
    main() #call goes to main step2

#draw this in notebook
#int/int=float
# float*100=float    

