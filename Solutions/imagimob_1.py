
#importing libraries
import time
import os 
import sys
import io
import pandas as pd
from statistics import mean 
from statistics import stdev 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import sklearn
from sklearn.cluster import KMeans
from sklearn import preprocessing


df = pd.read_csv('file_path') #please provide a path to the file
print('Raw DataFrame') 
print('******************************************************************')
print(df)

#saving the dataframe in a csv file
df.to_csv('action_signal_raw.csv', index = None)

#Performing mean operation of features row wise in order to convert into a single feature column
data = df.iloc[:,1:len(df.columns)+1] #selecting the columns(features) for performing row wise mean operation
average = data.mean(axis=1) #finding the row wise mean
new_data = {'Time(Seconds)':df['Time (seconds)'],
            'f0':average}
new_df = pd.DataFrame(new_data)
print('Mean of the sensor data ')
print('*****************************************************************************')
print(new_df)

#preprocessing the data 
column = new_df['f0']
minimum=column.min()
maximum=column.max()
new_df['f0'] = new_df['f0']/maximum
print('Below is the mean value of the standardised data')
print('*********************************')
print(new_df)

#performing clustering for categorizing the data based on the sensor values
#finding optimal value for number of clusters using within cluster sum of squares 

data = new_df.iloc[:,1:]
wcss = [] #empty list for calculating wcss after each iter
for i in range(1,50):
  kmeans =KMeans(i) 
  kmeans.fit(data)  
  wcss_iter = kmeans.inertia_
  wcss.append(wcss_iter)

print('below is the list of the within cluster sum of squares ')
print(wcss)

# We now use the elbow method to predict the number of clusters requires
number_of_clusters = range(1,50)
plt.plot(number_of_clusters,wcss)
plt.title('The Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Within-cluster-sum-of-squares')

#results from clustering 
kmeans_new = KMeans(7)
identified_clusters = kmeans_new.fit_predict(data) #predicting dependent of time
new_df['Cluster'] = identified_clusters
print('identified cluster groups labels')
print('************************************')
print(new_df)
print('************************************')

# Grouping of clusters
total_time= [] #dictionary for storing the total time
time_length = [] # dictionary for storing the average time length
label_list=[]
for i in range(len(length)):
  label_list.append('action')
  lt= []
  sum = 0
  index = new_df[new_df['Cluster'] == i].index.tolist()
  for j in index :
    sum = sum + new_df['Time(Seconds)'][j] # total time in a cluster 
    lt.append(new_df['Time(Seconds)'][j])
  time_length.append(mean(lt)) #performing standard deviation in order to find the standard length/duration of the time of a cluster
  total_time.append(sum)
  index_list.append(index)

output_data = {'Time(Seconds)':total_time,'Length(Seconds)':time_length,'Label(String)':label_list}
op_df = pd.DataFrame(output_data)
print('Output DataFrame')
print('***********************************************************************************')
op_df.sort_values("Time(Seconds)", axis = 0, ascending = True, 
                 inplace = True, na_position ='last')
print(op_df)