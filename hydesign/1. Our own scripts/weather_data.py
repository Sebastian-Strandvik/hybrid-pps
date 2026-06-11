# Importing things
    

import os
import time
import yaml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../examples/Europe/GWA2/input_ts_Workum_NLR.csv')

df["time"] = pd.to_datetime(df["Unnamed: 0"])
WS_150 = df["WS_150"]
price = df["Price"]



plt.hist(df.iloc[:, 4])
plt.xlabel("Wind speed [m/s]")
plt.ylabel("Frequency [hours/year]")
plt.title("Histogram for Wind Speed at hub height 150 m")
plt.show()

print("Mean of WS_150:", round(WS_150.mean(), 2))
print("Standard deviation of WS_150", round(WS_150.std(), 2))

#plt.hist(df.iloc[:, 2])
#plt.show()