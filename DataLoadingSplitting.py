import pandas as pd

def main():
    df=pd.read_csv("iris.csv")#same current directory
    print("Dataset loaded successfully!!")
    print("Dimensios of dataset is:",df.shape)#150 5 dimesnions of rows and cols of dataframe
    
    print(df["variety"])
    # print(df["sepal.length"].head())

    df["variety"]=df["variety"].map({'setosa':0 ,'versicolor':1,'virginica':2})#encoding and it is case sensitive
    #encoding used for alphanumeric to numeric
    print(df["variety"])

    X=df.drop("variety",axis='columns')#vertical ubha use of axis? 
    Y=df["variety"]

    print("Indepenedent variable dimensions:",X.shape)
    print("Dependent variable dimension:",Y.shape)



if __name__=="__main__":
    main()    