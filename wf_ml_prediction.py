import os
import pickle


def run_pred(input):
    models=["finalized_GB_model.sav","finalized_RF_model.sav","finalized_KNN_model.sav"]
    out={}
    for m in models:
        filename="models/"+m
        model = pickle.load(open(filename, 'rb'))
        result = model.predict(input)
        out[m]=result
    return out