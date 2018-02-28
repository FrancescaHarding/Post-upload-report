# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:26:23 2018

@author: Francesca
"""

import os
import pandas as pd


##Duplicate data

#check the current working directory, set directory to the location of files to be analysed
os.getcwd()
directory_duplicate = r'C:\\Users\\Francesca\\OneDrive\\Missing_data\\all_raw_files'
os.chdir(directory_duplicate)

#import all csv files in driectory, create list of dataframes,and merge into one dataframe
dfs = [pd.read_csv(f,names=["Date", "Time", "pH", "v0", "v1", "v2", "v3"]) 
                    for f in os.listdir(os.getcwd()) if f.endswith('csv')]
duplicate_data = pd.concat(dfs, axis=0, join='outer', ignore_index=True)

#delete outside columns (INITIAL ANALYSIS ONLY )
columns = ['v0','v1','v2','v3']
duplicate_data_shrunk = duplicate_data.drop(columns, axis=1)

#remove any times which have been recorded incorrectly 
duplicate_data_clean = duplicate_data_shrunk[duplicate_data_shrunk.Time <= '23:59:59']

#add a column to indicate if two measurements taken at the same time
duplicate_data_clean['Duplicate'] = duplicate_data_clean.duplicated()
duplicated_data = duplicate_data_clean[duplicate_data_clean.Duplicate == True]

#creating timestamp column by merging date and time, then converting into datetime object
duplicate_data_shrunk['Timestamp']= duplicate_data_shrunk['Date'] + '' + duplicate_data_shrunk['Time']
duplicate_data_shrunk['Timestamp']= pd.to_datetime(duplicate_data_shrunk['Timestamp'], errors='coerce')
duplicate_data_shrunk['Date']= pd.to_datetime(duplicate_data_shrunk['Date'], errors='coerce')
duplicate_data_shrunk['Time']= pd.to_datetime(duplicate_data_shrunk['Time'], errors='coerce')
duplicate_data_final= duplicate_data_shrunk.dropna(axis=0, how='any')

#other possible methods for converting into datetime object
#for i in duplicate_data_shrunk['Timestamp']:
#    try:
#        valid_date = pd.to_datetime(i)
#        print(valid_date)
#    except ValueError:
#        print('Invalid time')
#    continue

#def test_apply(x):
#    try:
#        return pd.to_datetime(x)
#    except ValueError:
#        return None
#cleanDF = duplicate_data_shrunk['Timestamp'].apply(test_apply).dropna()

##Battery depletion model
#add new directory for location of battery data, change to this directory 
battery_data_location = r'C:\\Users\\Francesca\\OneDrive\\Battery modelling\\updated_data.csv'
battery_data = pd.read_csv(battery_data_location, header = 0, index_col = 0)
battery_data['day'] = pd.to_datetime(battery_data['day'])




  