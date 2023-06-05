
#Data Munging
#Code test for Geo
#By D. Jenkins-Ferrett

import pandas as pd
import matplotlib.pyplot as plt

class DataMunger:
    """ Class to read in data from a text file, peform some aspects of
    cleaning the data, peform some basic calculations on the data and
    display the data in text and graph form. Pandas and pyplot from
    Matplotlib libraries are dependencies """

    def __init__(self, filepath, separator, header, skiprows, usecols):
        self.data = pd.read_csv(filepath, 
                                delimiter = separator,
                                header = header,
                                skiprows = skiprows,
                                usecols = usecols,
                                encoding = 'utf8')
        self.data.dropna(axis = 0, inplace = True)
        
    def __str__(self):
        return f'DataMunger({self.filepath})'

    def clean(self, cols, remove):
        """Removes a specified character from a specified column of data"""
        for col in cols:
            self.data[col] = self.data[col].str.replace(remove, '', regex = True)
            
    def typecast(self, typelist):
        """Uses a dictionary of column/type pairs to specify data types for columns"""
        self.data = self.data.astype(typelist)

    def display(self):
        """Prints the contents of the dataframe to the console with the index column"""
        print(self.data.to_string(index = False))
        
    def get_data(self, row, col):
        return self.data.iloc[row, col]
        """Returns an item from the dataframe at a specified row and column"""
        
    def maxval(self, col):
        """Returns the maximum value in a specified column of the dataframe"""
        self.maxval = self.data.max(axis = 0)[col]
        return self.maxval
        
    def minval(self, col):
        """Returns the minimum value in a specified column of the dataframe"""
        self.minval = self.data.min(axis = 0)[col]
        return self.minval
        
    def mindiff(self, col1, col2):
        """Returns the index of the row with the smallest difference in the values in two specified columns"""
        self.min_diff_idx = (abs(self.data[col1] - self.data[col2])).idxmin()
        return self.min_diff_idx
        
    def barplot(self, title, title_size, xaxis, yaxis, xlabel, ylabel ):
        """Plots a barplot using specifie columns from the dataframe as axes using
        specified title and axes labels"""
        plt.title(title, fontsize = title_size);
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        self.x_axis = range(len(self.data[xaxis]))
        plt.bar(self.x_axis, self.data[yaxis])
        plt.xticks(self.x_axis, self.data[xaxis])
        plt.show()

#weather
weather_data = DataMunger('weather.dat', '\s+', (0), [32], [0, 1, 2, 3])
weather_data.clean(['MxT', 'MnT'], '*')
weather_data.typecast({'Dy':'int', 'MxT': 'int', 'MnT': 'int'})
weather_data.display()
print('The minimum temperature is {} degrees fahrenheit.'.format(weather_data.minval('MnT')))
print('The maximum temperature is {} degrees fahrenheit.'.format(weather_data.maxval('MxT')))
print('The day with the smallest temperature difference is day {}.'.format(weather_data.get_data(weather_data.mindiff('MxT', 'MnT'), 0)))
weather_data.barplot('Morristown, NJ - June 2002', 24, 'Dy', 'AvT', 'Day of Month', 'Average Temperature (Degrees Fahrenheit)')

#football
football_data = DataMunger('football.dat', '\s+', None, [0], [1, 6, 8])
print('The team with the smallest difference between for and against goals is {}'.format(football_data.get_data(football_data.mindiff(6, 8), 0)))