from sklearn.datasets import load_iris

def main():
    dataset=load_iris()

    Line="-"*45
    print("Elements from the dataset are:")

    print(Line)
    for i in range(len(dataset.target)):#label encoding
        print("Id: %d ,Features: %s,Labels: %s" % (i,dataset.data[i],dataset.target[i]))
        #%d=   %s=
   


if __name__=="__main__":
    main()