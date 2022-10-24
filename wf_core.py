import pandas as pd
import numpy as np

from wf_dataprocessing import load_data,preprocess
from wf_visualization import visualize

pathData="data_original/dataset.csv"
savePath="data_processing/"

data=load_data(pathData)
data=preprocess(data,savePath)
visualize(data)