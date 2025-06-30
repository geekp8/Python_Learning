class Employee:
    CompanyName="Marvellous"#class variable 
    #not created inside init

    def __init__(self,A,B,C):#default constructor with params 
        print("Inside constructor")
        self.Name=A
        self.Salary=B
        self.City=C

    def __del__(self):
        print("Inside destructor")

def main():
    print("Class variable:"+Employee.CompanyName)

    emp1=Employee('Rahul',15000,'Pune')
    emp2=Employee('Pooja',25000,'Mumbai')#single quote string allowed both also

    
    #print("")
    print("Employee name:"+emp1.Name)
    print("Employee Salary:",emp1.Salary)#int sathi comma
    print("Employee city:"+emp1.City)

if __name__=="__main__":
    main()
