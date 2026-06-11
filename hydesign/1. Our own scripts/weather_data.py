# Importing things
    

import os
import time
import yaml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Colors

from cycler import cycler
import matplotlib as mpl
plt.style.use('default')
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = ' '
mpl.rcParams['lines.marker'] = '.'
mpl.rcParams['xtick.labelsize'] = 15
mpl.rcParams['ytick.labelsize'] = 15
mpl.rcParams['axes.labelsize'] = 15
mpl.rcParams['legend.fontsize'] = 15
mpl.rcParams['axes.prop_cycle'] = cycler(color=["#2F3EEA", "#1FD082", "#030F4F", "#F6D04D", "#FC7634", "#E83F48", "#008835", "#79238E"])
DTU_colors = ["#2F3EEA", "#1FD082", "#030F4F", "#F6D04D", "#FC7634", "#E83F48", "#008835", "#79238E"]


df = pd.read_csv('../examples/Europe/GWA2/input_ts_Workum_NLR.csv')

df["time"] = pd.to_datetime(df["Unnamed: 0"])
WS_150 = df["WS_150"]
Price = df["Price"]
DNI = df["dni"]
GHI = df["ghi"]
WS_100 = df["WS_100"]
WS_50 = df["WS_50"]

# Wind speed at 150 m hub height

plt.hist(df.iloc[:, 4])
plt.xlabel("Wind speed [m/s]")
plt.ylabel("Frequency [hours/year]")
plt.title("Histogram for Wind Speed at hub height 150 m")
plt.show()

print("Mean of WS_150:", round(WS_150.mean(), 2))
print("Standard deviation of WS_150", round(WS_150.std(), 2))

# Price

plt.hist(df.iloc[:, 15])
plt.xlabel("Electricity price [€/MWh]")
plt.ylabel("Frequency [hours/year]")
plt.title("Histogram for electricity price throughout a year")
plt.show()

print("Mean of electricity price:", round(Price.mean(), 2))
print("Standard deviation of electricituy price", round(Price.std(), 2))

# DNI

plt.hist(df.iloc[:, 13])
plt.xlabel("Direct normal irradtion [W/m2]")
plt.ylabel("Frequency [hours/year]")
plt.title("Histogram for DNI throughout a year")
plt.show()

print("Mean of DNI:", round(DNI.mean(), 2))
print("Standard deviation of DNI", round(DNI.std(), 2))

# Correlation

fig, axs = plt.subplots(4, 4, figsize=(20,20))

for i_col in range(4):
    x_axis_values = df.iloc[:, i_col+1]
    axs[i_col, 0].scatter(x_axis_values, GHI.values, color=DTU_colors[i_col] )
    axs[i_col, 0].text(1, 5, f'Corr: {np.round(np.corrcoef(x_axis_values, GHI.values)[0,1], 3)}', fontsize=15 , color='darkviolet')

    axs[i_col, 1].scatter(x_axis_values, WS_100.values, color=DTU_colors[i_col] )
    axs[i_col, 1].text(0.5, 6, f'Corr: {np.round(np.corrcoef(x_axis_values, WS_100.values)[0,1], 3)}', fontsize=15, color='darkviolet' )

    axs[i_col, 2].scatter(x_axis_values, Price.values, color=DTU_colors[i_col] )
    axs[i_col, 2].text(0.5, 5, f'Corr: {np.round(np.corrcoef(x_axis_values, Price.values)[0,1], 3)}', fontsize=15, color='darkviolet' )

    axs[i_col, 3].scatter(x_axis_values, WS_50.values, color=DTU_colors[i_col] )
    axs[i_col, 3].text(0.5, 7, f'Corr: {np.round(np.corrcoef(x_axis_values, WS_50.values)[0,1], 3)}', fontsize=15, color='darkviolet' )

fig, axs = plt.subplots(4, 4, figsize=(20, 20))

variables = [GHI, WS_100, Price, WS_50]
names = ['GHI', 'WS_100', 'Price', 'WS_50']

for i in range(4):          # rows (y-axis)
    for j in range(4):      # columns (x-axis)

        x = variables[j].values
        y = variables[i].values

        axs[i, j].scatter(
            x,
            y,
            alpha=0.6,
            s=10,
            color=DTU_colors[i]
        )

        corr = np.corrcoef(x, y)[0, 1]

        axs[i, j].text(
            0.05, 0.95,
            f'Corr: {corr:.3f}',
            transform=axs[i, j].transAxes,
            va='top',
            fontsize=12,
            color='darkviolet'
        )

        # Column titles
        if i == 0:
            axs[i, j].set_title(names[j], fontsize=14)

        # Row labels
        if j == 0:
            axs[i, j].set_ylabel(names[i], fontsize=14)

        # Only bottom row gets x-labels
        if i == 3:
            axs[i, j].set_xlabel(names[j], fontsize=14)

plt.tight_layout()
plt.show()