
#Football

import pandas as pd

df = pd.read_csv('football.dat', delimiter = '\s+', header = None, skiprows = 1, usecols = [1, 6, 8], encoding = 'utf8')
df.dropna(axis = 0, inplace = True)
small_diff_idx = (abs(df[6] - df[8])).idxmin()
print('The team with the smallest difference between for and against goals is {}'.format(df.iat[small_diff_idx, 0]))