# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 01:41:43 2021

@author: pc
"""

import pandas as pd
dataset = data = pd.read_csv("TwitterUsers.csv") #, nrows=6
#print(dataset)
#len(dataset) 

# ADD all columns values in one column**************
# ADD a new column dataset['newColumn'] = x

# / num of columns + no added / max() *100
# columns = 5, (3 + 10(weightage of followers) + 2(weightage of friends))

x = dataset['Number of followers'] * 10 #first column which has numbers AND Number of followers has a higher weightage so we multiplied by 10 

for column in dataset.columns:
    if (column != 'username' and column != 'Number of followers') : 
        if (column == 'Number of friends'):
            #print(dataset[column])
            
            #print('true------------------')
            x = x + dataset[column] * 2
        else:
            x = x + dataset[column]
        #print('new x', x)

dataset['rank'] = x

# print(dataset)

dataset['rank'] = dataset['rank'] / 15
#print(dataset['rank'])
i = 0
for value in dataset['rank']:
    #print(value, dataset['rank'][i])
    dataset['rank'][i] = int(dataset['rank'][i]) 
    i = i+1
#print(dataset['rank'])

#For finding out rank, we divide all by the highest number value in the list and * 100 for percentage
dataset['rank'] = dataset['rank'] / max(dataset['rank']) * 100
i = 0
for value in dataset['rank']:
    #print(value, dataset['rank'][i])
    dataset['rank'][i] = int(dataset['rank'][i]) 
    i = i+1

#print(dataset['rank'])

print('dataset.head: ')
print(dataset[['username', 'rank']].head())

# Ranking of all users in percentage











