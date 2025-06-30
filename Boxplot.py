import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df=pd.read_csv("iris.csv")

    #plt.boxplot(df['sepal.length'],bins=10,color="skyblue",edgecolor='black')

    sns.boxplot(x="variety",y="petal.length",data=df)

    plt.title("Marvellous Boxplot for Petal Length by Variety")

    plt.show()#for showing diagram

    


if __name__=="__main__":
    main()