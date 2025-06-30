#user defined function 

def Help(no):
    print("Inside Help")
    no=no + 1
    return no

value=10#execution will start from line 6 and I am sending integer
i=Help(value)
print("i contains:",i)


