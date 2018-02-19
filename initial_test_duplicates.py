# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd

#check the current working directory, set directory to the location of files to be analysed
os.getcwd()
directory = r'C:\\Users\\Francesca\\OneDrive\\Missing_data\\all_raw_files'
os.chdir(directory)


#import all csv files in driectory, create list of dataframes,and merge into one dataframe
dfs = [pd.read_csv(f,names=["Date", "Time", "pH", "v0", "v1", "v2", "v3"]) 
                    for f in os.listdir(os.getcwd()) if f.endswith('csv')]

final_data = pd.concat(dfs, axis=0, join='outer', ignore_index=True)

#delete outside columns (INITIAL ANALYSIS ONLY )
columns = ['v0','v1','v2','v3']
final_data_shrunk = final_data.drop(columns, axis=1)

#remove any times which have been recorded incorrectly 
subset_data = final_data_shrunk[final_data_shrunk.Time <= '23:59:59']

#looks for duplicate rows in dataframe and stores bool values as data series
final_data_shrunk['Duplicate'] = final_data_shrunk.duplicated()
final_data_shrunk[final_data_shrunk.Duplicate == True]

#create a timestamp column by merging date and time, and then removing this from final data frame
final_data_shrunk['Timestamp'] = final_data_shrunk['Date'] + '' + final_data_shrunk['Time']
final_data_shrunk = final_data_shrunk.drop('Date', axis=1)
final_data_shrunk = final_data_shrunk.drop('Time', axis=1)


