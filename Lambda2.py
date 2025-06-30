def ChkNum(value):
   # value=int(input("Enter number"))
    if (value%2==0):
        return True
        #print("Even")
    else:
        return False
        #print("Odd")

ret=ChkNum(10)

if ret==True:
    print("Number is even")
else:
    print("Number is odd")


  

