from sklearn.metrics import confusion_matrix

def main():
    Actual=[1,0,1,1,0,1,0,1,1,0]
    Predicted=[1,0,1,0,0,1,1,1,1,1]

    Con_Mat=confusion_matrix(Actual,Predicted)

    #TN  FP
    #FN  TP   
#0=N
#  [2 2]
#  [1 5]

    print("Confusion Matris is:")
    print(Con_Mat)

    #Accuracy= TN+TP/(TN+FP+TP+FN)

if __name__=="__main__":
    main()