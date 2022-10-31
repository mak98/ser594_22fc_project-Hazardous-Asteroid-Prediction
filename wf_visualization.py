import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize(data):
    qtData=["diameter","H","a"]
    tdata="Quantitative Data (3):\n"
    for i in qtData:
        print("For ",i,":")
        print("Minium value=",min(data[i]))
        print("Maximum value=",max(data[i]))
        print("Median value=",data[i].median())
        tdata+="For "+i+":"+"\n"+"Minium value="+str(min(data[i]))+"\n"+"Maximum value="+str(max(data[i]))+"\n"+"Median value="+str(data[i].median())+"\n"
    tdata+="\nQualitative Data (2):\n"
    qlData=["neo","class"]
    for i in qlData:
        print("For ",i,":")
        print("Number of Categories:",len(data[i].unique()))
        print("Most Occuring Category=",data[i].value_counts().idxmax())
        print("Least Occuring Category=",data[i].value_counts().idxmin())
        tdata+="For "+i+":"+"\n"+"Number of Categories:"+str(len(data[i].unique()))+"\n"+"Most Occuring Category="+str(data[i].value_counts().idxmax())+"\n"+"Least Occuring Category="+str(data[i].value_counts().idxmin())+"\n"
    with open("data_processing/summary.txt",'w') as f:
        f.write(tdata)
    corMat=np.zeros((3,3))
    for i in range(3):
        for j in range(i,3):
            corMat[i][j]=data[qtData[i]].corr(data[qtData[j]])
    print(corMat)
    np.savetxt("data_processing/correlations.txt",corMat)
    
    for i in range(3):
        for j in range(i+1,3):
            col1=qtData[i]
            col2=qtData[j]
            x=data[col1]
            y=data[col2]
            if col2=="a":#Removing outliers just for better visual
                    x=data[data[col2]<10**10][col1]
                    y=y[y<10**10]
            sName=col1+" vs "+col2
            plt.scatter(x,y)
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title(sName)
            plt.savefig("visuals/"+sName+".png")
            plt.show()
    for i in qlData:
        data[i].hist()
        plt.title("Histogram for "+i)
        plt.savefig("visuals/"+i+".png")
        plt.show()
    return None