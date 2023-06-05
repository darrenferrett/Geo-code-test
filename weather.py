
#Weather

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.dat', delimiter = '\s+', header = (0), usecols = ['Dy','MxT','MnT','AvT'], encoding = 'utf8')

df.drop(index = df.index[-1], axis = 0, inplace = True)
df['MxT'] = df['MxT'].str.replace('*', '', regex = True)
df['MnT'] = df['MnT'].str.replace('*', '', regex = True)
df = df.astype({'Dy':'int', 'MxT': 'int', 'MnT': 'int'})
print(df.to_string(index = False))

max_temp = df.max(axis = 0)['MxT']
min_temp = df.min(axis = 0)['MnT']

print('Min temp is {}'.format(min_temp))
print('Max temp is {}'.format(max_temp))

small_diff_idx = (df['MxT'] - df['MnT']).idxmin()
print('The day of the month with the smallest temperature difference is day {}'.format(df.iat[small_diff_idx, 0]))

plt.title('Morristown, NJ - June 2002', fontsize = 24)
plt.xlabel('Day of Month')
plt.ylabel('Average Temperature (Degrees Fahrenheit)')
x_axis = range(len(df['Dy']))
plt.bar(x_axis, df['AvT'])
plt.xticks(fontsize = 8)
plt.xticks(x_axis, df['Dy'])
plt.show()

    
