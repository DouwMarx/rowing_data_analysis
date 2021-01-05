import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal as s

from matplotlib.backends.backend_pdf import PdfPages

"""A not so very neat script for some initial data exploration"""

fnames = ["Sensor_record_20201204_113103_AndroSensor.csv",
         "Sensor_record_20201205_155404_AndroSensor.csv",
         "Sensor_record_20201206_165254_AndroSensor.csv",
          "Sensor_record_20201207_114856_AndroSensor.csv"]

# Load a particular dataset
fname = fnames[3]
d = pd.read_csv("/run/media/douwmarx/DATA/Data/rowing_data/" + fname)

pp = PdfPages(fname[0:-4]+'.pdf')

# List the channels measured
for k in d.keys():
    print(k)


def plot_spectogram(signal):

    # Apply a wiener filter
    fs = 1/(10*1E-3)  # 100Hz sampling rate
    print(fs)
    plt.figure()
    f, t, Sxx = s.spectrogram(signal, fs, nperseg=30000) # 1 segment is a 5 minuit
    plt.pcolormesh(t, f, np.log(Sxx**2))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.ylim(0,2)
    plt.show()
    return

def butter_lowpass_filter(data, cutoff, fs, order):
    nyq = 0.5 * fs  # Nyquist Frequency
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients
    b, a = s.butter(order, normal_cutoff, btype='low', analog=False)
    y = s.filtfilt(b, a, data)
    return y


acc_xyz = ["ACCELEROMETER X (m/s²)", "ACCELEROMETER Y (m/s²)", "ACCELEROMETER Z (m/s²)"]
gyro_xyz = ["GYROSCOPE X (rad/s)", "GYROSCOPE Y (rad/s)", "GYROSCOPE Z (rad/s)"]
orientation_xyz = ["ORIENTATION Z (azimuth °)", "ORIENTATION X (pitch °)", "ORIENTATION Y (roll °)"]

for sig in gyro_xyz:

    # Low pass filter
    signal = butter_lowpass_filter(d[sig],2,100,5)
    plot_spectogram(signal)
    plt.title(sig)
    plt.savefig("../reports/figures/" + sig.replace(" ", "_").replace("(rad/s)","") + "_spectrogram.png")

# acc_mag = np.sqrt(d[acc_xyz[0]]**2 + d[acc_xyz[1]]**2 + d[acc_xyz[2]]**2)
#
# plt.figure()
# plt.plot(acc_mag)

# for k in acc_xyz:
#     plt.figure()
#     plt.title(k)
#     plt.plot(d[k])
#     pp.savefig()
#     print(k)
# pp.close()

# keys_to_check = ["ACCELEROMETER X (m/s²)",
# "ACCELEROMETER Y (m/s²)",
# "ACCELEROMETER Z (m/s²)",
# "GRAVITY X (m/s²)",
# "GRAVITY Y (m/s²)",
# "GRAVITY Z (m/s²)",
# "LINEAR ACCELERATION X (m/s²)",
# "LINEAR ACCELERATION Y (m/s²)",
# "LINEAR ACCELERATION Z (m/s²)",
# "GYROSCOPE X (rad/s)",
# "GYROSCOPE Y (rad/s)",
# "GYROSCOPE Z (rad/s)",
# "LIGHT (lux)",
# "MAGNETIC FIELD X (μT)",
# "MAGNETIC FIELD Y (μT)",
# "MAGNETIC FIELD Z (μT)",
# "ORIENTATION Z (azimuth °)",
# "ORIENTATION X (pitch °)",
# "ORIENTATION Y (roll °)]"]

# pd.set_option('display.width', 500)
# pd.set_option('precision', 3)
# crr = d.corr()
# print(crr)