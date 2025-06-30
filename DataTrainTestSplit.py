import pandas as pd
#import sklearn
from sklearn.model_selection import train_test_split


def main():
    df=pd.read_csv("iris.csv")#same current directory
    print("Dataset loaded successfully!!")
    
    
    print(df["variety"])
   

    df["variety"]=df["variety"].map({'setosa':0 ,'versicolor':1,'virginica':2})#encoding and it is case sensitive
   

    X=df.drop("variety",axis='columns')#vertical ubha use of axis for columns removal
    Y=df["variety"]

    #A C B D
    X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2)#import the train test split function

    print("Dimenion of X_train",X_train.shape)
    print("Dimenion of X_test",X_test.shape)
    print("Dimenion of Y_train",Y_train.shape)
    print("Dimenion of Y_test",Y_test.shape)



if __name__=="__main__":
    main()    