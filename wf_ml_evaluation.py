import pandas as pd
import numpy as np
import pickle

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from wf_dataprocessing import load_data,preprocess
from wf_ml_training import train_models
from wf_ml_prediction import run_pred
pathData="data_original/dataset.csv"
savePath="data_processing/"
modelPath="models/"

data=load_data(pathData)
data=preprocess(data,savePath)


x = data.drop('pha', axis=1)
y = data['pha']

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=0)

scaler = StandardScaler()
xTrain = scaler.fit_transform(xTrain)
xTest = scaler.transform(xTest)

KNNmodels,RandomForestModels,GradientBoostingModels= train_models(xTrain,yTrain)
summary=""
kl=[]
acc=[]
fscore=[]
print("Testing KNN")
summary+="For KNN models\n"
for k,model in KNNmodels.items():
    pred=model.predict(xTest)
    kl.append(k)
    accuracy=accuracy_score(yTest,pred)
    f1=f1_score(yTest,pred)
    fscore.append(f1)
    acc.append(accuracy)
    summary+=f'For K={k}\n accuracy: {accuracy}, f1 score: {f1}\n'

fig, axs = plt.subplots(2)
axs[0].plot(kl, fscore)
axs[1].plot(kl, acc)
axs[0].set_xlabel("K")
axs[0].set_ylabel("F1 Score")
axs[1].set_xlabel("K")
axs[1].set_ylabel("Accuracy")
plt.savefig("visuals/KNN_plot.png")
plt.show()
Kselected=kl[fscore.index(max(fscore))]
KNNmodel=KNNmodels[Kselected]
print("Model Selected: K=",Kselected)
print("F1 score on Test: ",max(fscore))

filename = modelPath+'finalized_KNN_model.sav'
f=open(filename,"wb")
pickle.dump(model, f)
f.close()
print("Model Saved")


nl=[]
fscore=[]
acc=[]
print("Testing Random Forest Models")
summary+="For Random Forest Models \n"
for n,model in RandomForestModels.items():
    pred=model.predict(xTest)
    nl.append(n)
    accuracy=accuracy_score(yTest,pred)
    f1=f1_score(yTest,pred)
    fscore.append(f1)
    acc.append(accuracy)
    summary+=f'For N={n}\n accuracy: {accuracy}, f1 score: {f1}\n'
fig, axs = plt.subplots(2)
axs[0].plot(nl, fscore)
axs[1].plot(nl, acc)
axs[0].set_xlabel("N")
axs[0].set_ylabel("F1 Score")
axs[1].set_xlabel("N")
axs[1].set_ylabel("Accuracy")
plt.savefig("visuals/RF_plot.png")

plt.show()
Nselected=nl[fscore.index(max(fscore))]
RandomForestmodel=RandomForestModels[Nselected]
print("Model Selected: N estimators=",Nselected)
print("F1 score on Test: ",max(fscore))
filename = modelPath+'finalized_RF_model.sav'
f=open(filename,"wb")
pickle.dump(model, f)
f.close()
print("Model Saved")


lr=[]
fscore=[]
acc=[]
print("Testing Gradient Boosting Models:")
summary+="For Gradient Boosting Models:\n"
for l,model in GradientBoostingModels.items():
    pred=model.predict(xTest)
    lr.append(l)
    accuracy=accuracy_score(yTest,pred)
    f1=f1_score(yTest,pred)
    fscore.append(f1)
    acc.append(accuracy)
    summary+=f'For LR={l}\n accuracy: {accuracy}, f1 score: {f1}\n'
fig, axs = plt.subplots(2)
axs[0].plot(lr, fscore)
axs[1].plot(lr, acc)
axs[0].set_xlabel("Learning Rate")
axs[0].set_ylabel("F1 Score")
axs[1].set_xlabel("Learning Rate")
axs[1].set_ylabel("Accuracy")
plt.savefig("visuals/GB_plot.png")

plt.show()
Lselected=lr[fscore.index(max(fscore))]
RandomForestmodel=GradientBoostingModels[Lselected]
print("Model Selected: N estimators=",Lselected)
print("F1 score on Test: ",max(fscore))
filename = modelPath+'finalized_GB_model.sav'
f=open(filename,"wb")
pickle.dump(model, f)
f.close()
print("Model Saved")
with open("evaluation/summary.txt",'w') as f:
    f.write(summary)

rawdata1=[3.4,939.4,0.09,2458600.5,0.0760090265983052,414267106.23553926,382779066.73887926,10.59406719506626,80.30553090445737,73.59769469844186,77.37209751948711,445755145.7321993,0.2138852265918273,2458238.7541293176,1683.145702657688,238579088.0,1,0,0,0,0,0,0,0,1,0,0,0,0]
rawdata2=[4.2,545.0,0.101,2459000.5,0.2299722588646258,414966678.65704536,319535854.2127334,34.83293159121413,173.0247412488342,310.2023924446679,144.9756754788195,510397503.1013574,0.213344586343708,2458320.9623657744,1687.410991624711,184649784.00000003,1,0,0,0,0,0,0,0,1,0,0,0,0]
data=[rawdata1,rawdata2]
output=run_pred(data)
print(output)

inputAy=scaler.transform(x.loc[x["neo_Y"]==1].to_numpy())
inputBy=scaler.transform(x.loc[x["class_APO"]==1].to_numpy())
inputAn=scaler.transform(x.loc[x["neo_Y"]==0].to_numpy())
inputBn=scaler.transform(x.loc[x["class_APO"]==0].to_numpy())

inputAyBn= scaler.transform(x.loc[(x["neo_Y"]==1) & (x["class_APO"]==0)].to_numpy())
inputAyBy= scaler.transform(x.loc[(x["neo_Y"]==1) & (x["class_APO"]==1)].to_numpy())

features={"neo_Y=1":inputAy,"class_APO=1":inputBy,"neo_Y=0":inputAn,"class_APO=0":inputBn,"neo_Y=1 and class_APO=0":inputAyBn,"neo_Y=1 and class_APO=1":inputAyBy}
for k,v in features.items():
    pred=run_pred(v)
    print("For",k)
    for m,p in pred.items():
        print("For ",m)
        count = pd.Series(p).value_counts()
        print(count)


