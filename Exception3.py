
# def main():
#     print("Enter first number : ")
#     no1 = int(input())

#     print("Enter second number : ")
#     no2 = int(input())

#     Ans = 0
#     try:
#         Ans = no1 / no2

#     except ZeroDivisionError as zobj:
#         print("Exception ocurred due to second input",zobj)
        
#     print("Division is : ",Ans)

# if __name__ == "__main__":
#     main()


def main():
    print("Enter first number: ")
    no1=int(input())

    print("Enter second number:")
    no2=int(input())

    Ans=0
    try:
        Ans=no1/no2

    except ZeroDivisionError as zobj:#add as obj of it
        print("Exception occured due to second input",zobj)

    print("Division is: ",Ans)

if __name__=="__main__":
    main()                    