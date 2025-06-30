class Circle:
    Pi=3.14


    def __init__(self,A):
        print("Inside Circle constructor")
        self.Radius=A

    def CalculateArea(self):
        Ans=0.0
        Ans=Circle.Pi*self.Radius*self.Radius
        return Ans

class CircleX(Circle):#inheried from Circle in ()
    def __init__(self,A):
        print("Inside CircleX constructor")
        super().__init__(A)#one level up

    def CalculateCircumference(self):
            Ans=0.0
            Ans=2* Circle.Pi*self.Radius
            return Ans

def main():
    obj=CircleX(10.5)

    ret=obj.CalculateArea()
    print("area of circle is:",ret)
    ret=obj.CalculateCircumference()
    print("Circumference of circle is",ret)
    #print("Area of circle is:",Ret)
if __name__=="__main__":
    main()