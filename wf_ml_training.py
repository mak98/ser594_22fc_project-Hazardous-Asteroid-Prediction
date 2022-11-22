from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

def train_KNN(kRange,xTrain,yTrain):
    KNNmodels={}
    print("Training KNN models")
    for k in range(3,kRange,2):
        print("K=",k)
        model=KNeighborsClassifier(n_neighbors=k)
        model.fit(xTrain,yTrain)
        KNNmodels[k]=model
    return KNNmodels
def train_RandomForest(estimatorRange,xTrain,yTrain):
    RandomForestModels={}
    print("Training RandomForest models")
    for n in range(10,estimatorRange,10):
        print("Number of Estimators",n)
        model=RandomForestClassifier(n_estimators=n)
        model.fit(xTrain,yTrain)
        RandomForestModels[n]=model
    return RandomForestModels
def train_GradientBoosting(xTrain,yTrain):
    print("Training Gradient Boosting models")
    lr=[0.001,0.01,0.05,0.1,0.15]
    GradientBoostingModels={}
    for l in lr:
            print("Learning Rate",l)
            model=GradientBoostingClassifier(learning_rate=l)
            model.fit(xTrain,yTrain)
            GradientBoostingModels[l]=model
    return GradientBoostingModels
            
def train_models(xTrain,yTrain):
    KNNmodels=train_KNN(20,xTrain,yTrain)
    RandomForestModels=train_RandomForest(100,xTrain,yTrain)
    GradientBoostingModels=train_GradientBoosting(xTrain,yTrain)
    return KNNmodels,RandomForestModels,GradientBoostingModels