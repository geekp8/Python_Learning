a=5
#b=0#Zerodivisonerror
b=2




try:
    print("Resource open")
    print(a/b)

    k=int(input("Enter number:"))
    print(k)
    #print("Resource closed")#wont work here as line 7 will go to 12
#except Exception:#will execute only when we have the error

except ZeroDivisionError as e:
    print("Hey you cannot divide a number by zero",e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went wrong..")
    #print("Resource closed") 


finally:#will execute even if you dont get the exception
    print("Resource closed")
print("Bye")

