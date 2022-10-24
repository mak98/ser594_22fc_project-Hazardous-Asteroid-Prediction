import pandas as pd
import numpy as np

def load_data(path):
    data=pd.read_csv(path,low_memory=False)
    return data
def preprocess(data,savePath):
    au=1.496*10**8
    print("Initial Dataset Loaded Info:")
    print(data.shape)
    print(data.info())
    print(data.isnull().sum())
    data = data.drop(['name', 'prefix','id', 'spkid','full_name', 'equinox','orbit_id','pdes','epoch_mjd','epoch_cal','rms','per_y','tp_cal'], axis=1)#while these fields may be useful for us to undearstand about which object we are talking about, they dont have much to contribute about actual details about the nature of object.
    data= data.dropna()
    #Since sigma is just uncertainity values we dont need them for visualization.
    for i in data.columns:
        if "sigma" in i:
            data.pop(i)
        if "ld" in i:
            data.pop(i)
    #Converting Astronomical unit to Km
    data['a'] = data['a'].apply(lambda x: x*au)
    data['q'] = data['q'].apply(lambda x: x*au)
    data['ad'] = data['ad'].apply(lambda x: x*au)
    data['moid'] = data['moid'].apply(lambda x: x*au)

    print("Dataset after cleaning:")
    print(data.shape)
    print(data.info())
    print(data.head())
    pd.DataFrame.to_csv(data,savePath+"processed_dataset.csv")
    return data
