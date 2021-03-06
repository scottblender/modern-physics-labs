import pandas as pd
import numpy as np
data = pd.read_csv("/Users/scottblender/Desktop/photoelectric-effect-data.csv")
frequency_df = data['Frequency ']
print(frequency_df.head())
avg_stopping_potential = data['Average ']
print(avg_stopping_potential.head())
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
X = frequency_df
Y = avg_stopping_potential
result = stats.linregress(X,Y)
line = result.slope*X+result.intercept
print(result.stderr)
print(result.slope)
print(result.intercept)
e = -1.602*(10 ** -19)
h = (e*result.slope) * (10 ** -14)
print(h)
plt.scatter(frequency_df, avg_stopping_potential)
plt.plot(frequency_df, line, 'r', label='$y=%3.7s*x+%3.7s$'%(result.slope, result.intercept))
plt.xlabel('Frequency (Hz * $10^{14}$)')
plt.ylabel('Stopping Potential (V)')
plt.title('Frequency (Hz * $10^{14}$) vs Stopping Potential (V)')
plt.legend(fontsize=9)
plt.show()