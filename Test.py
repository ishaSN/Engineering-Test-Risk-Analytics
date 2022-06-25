#!/usr/bin/env python
# coding: utf-8

# In[542]:


#Importing required libraries
import pandas as pd
import glob, os
import re


# In[549]:


# importing required modules
from zipfile import ZipFile
  
# specifying the name of the zip file which is given for the task
file_name = "Engineering_Test_Risk_Analytics.zip"
  
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
  
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')


# In[551]:


#Removing the file combined.csv so that the task can be continued even after removing or adding a new file.
os.remove('D:/Engineering_Test_Risk_Analytics/Engineering Test Risk Analytics/combined.csv')


# In[552]:


# Collect the .csv files and give command to create one column by assigning respective file name to each row of each file
files = glob.glob('D:/Engineering_Test_Risk_Analytics/Engineering Test Risk Analytics/*.csv')
print (files)
#['samples_for_so//a.csv', 'samples_for_so//b.csv', 'samples_for_so//c.csv']
df = pd.concat([pd.read_csv(fp).assign(Environment=os.path.basename (fp).split(' ')[0])
       for fp in files])
df = df.drop(["Count","Events per Second","Events / Second"], axis=1)
df = df.dropna(axis=0)


# In[553]:


# drop duplicates, reset index and sort values 

import pandas as pd
df = df.drop_duplicates(subset=None, keep='first')
df = df.reset_index(drop=True)
df = df.sort_values(by='Environment', axis=0, ascending=False)
df['Environment'] = df['Environment'].astype(str) + " " + "Prod"
df


# In[554]:


# create a new .csv file named combine.csv
df.to_csv("D:/Engineering_Test_Risk_Analytics/Engineering Test Risk Analytics/combined.csv",index=False)


# In[555]:


df.dtypes


# In[556]:


# creating and saving the zip file 

def get_all_file_paths(directory):
  
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths        
  
def main():
    # path to folder which needs to be zipped
    directory = './python_files'
  
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)
  
    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
  
    # writing files to a zipfile
    with ZipFile('Engineering_Test_Risk_Analytics.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
  
    print('All files zipped successfully!')         
  
if __name__ == "__main__":
           main()


# In[ ]:




