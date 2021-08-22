import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import time 
import pandas as pd

path_file = "../data/churndata.csv"

df = pd.read_csv(path_file)
#??pd.read_csv

#print(df.head(df))

print(df.columns)

churn = df['Churn']

#print(churn.value_counts())

print(df.groupby(['Churn', 'gender', 'SeniorCitizen']).count())