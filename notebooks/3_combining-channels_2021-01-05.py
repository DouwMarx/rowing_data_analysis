import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

d = pd.read_csv("../data/Sensor_record_20201126_164859_AndroSensor.csv")
print(d.keys())

acc = d['ACCELEROMETER X (m/s²)'].values + d['ACCELEROMETER Y (m/s²)'].values +d['ACCELEROMETER Z (m/s²)'].values

# plt.figure()
# # plt.plot(d['Time since start in ms '].values,d['ACCELEROMETER X (m/s²)'].values)
# # plt.plot(d['Time since start in ms '].values,d['ACCELEROMETER Y (m/s²)'].values)
# # plt.plot(d['Time since start in ms '].values,d['ACCELEROMETER Z (m/s²)'].values)
# plt.scatter(d['Time since start in ms '].values,acc)
# plt.show()
#
# fft = np.fft.fft(acc)
# plt.figure()
# plt.plot(fft[0:int(len(fft)/2)])
# plt.show()

# plt.figure()
# plt.plot(d['Time since start in ms '].values,d["LIGHT (lux)"].values)
# plt.show()
d = np.diff(d['Time since start in ms '].values)
print(np.average(d))
print(np.std(d))
