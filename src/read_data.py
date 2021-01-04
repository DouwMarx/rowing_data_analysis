import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d = pd.read_csv("../data/a_20201126.csv")

print(d.head())
print(d.keys())

plt.figure()

# For getting time from the data stamp
np.array([x[-3:] for x in d["YYYY-MO-DD HH-MI-SS_SSS"][0:10].values]).astype("float")