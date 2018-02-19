# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:26:23 2018

@author: Francesca
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
final_data_clean = final_data_shrunk[final_data_shrunk.Time <= '23:59:59']

#add a column to indicate if two measurements taken at the same time
final_data_clean['Duplicate'] = final_data_clean.duplicated()
duplicated_data = final_data_clean[final_data_clean.Duplicate == True]

