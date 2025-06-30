def fact(n):
    #for i in range()
    #5*4!
    #n* fact(n-1)
    #0!=1
    if (n==0):
        return 1
    return  n *fact(n-1)

no=int(input("Enter number:"))
result=fact(no)

print("Factorial:",result)
