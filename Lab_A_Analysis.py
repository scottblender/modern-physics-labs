from sys import stderr
import pandas as pd
import numpy as np
data = pd.read_csv("/Users/scottblender/Desktop/lab_a.csv")
radiation_counts_df = data['Radiation']
radiation_counts_df = radiation_counts_df[radiation_counts_df > 9 ]
time_df = data['Time']
avg_background_counts = 1.696 
radiation_counts_df = np.log(radiation_counts_df)
time_df = time_df[time_df >= 290]
time_df= time_df[time_df <= 952]
print(time_df)
print(radiation_counts_df)
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
X = time_df
Y = radiation_counts_df
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(X,Y)
line = slope*X+intercept
print(slope_std_error)
plt.plot(time_df, radiation_counts_df)
plt.plot(time_df, line, 'r', label='$y=%3.7s*x+%3.7s$'%(slope, intercept))
plt.xlabel('Time (s)')
plt.ylabel('ln Radiation (counts)')
plt.title('Radioactive Decay of Ba-137m - Time(s) vs ln Radition (counts)')
plt.legend(fontsize=9)
plt.show()