#!/usr/bin/env python3

import csv
import numpy as np
import pandas
import math
from sklearn.neighbors import NearestNeighbors
from collections import Counter

def distance(x1,y1,x2,y2):
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist

filename = 'train.csv'

csvreader = csv.DictReader(open(filename,'r'), delimiter = ',')
sample=[]
#print(csvreader.line_num)
for i,line in enumerate(csvreader):
    sample.append([line[key] for key in csvreader.fieldnames])
    if i==10:
        break
sample = np.array(sample).astype(float)
#print(csvreader.fieldnames)

rowID = sample[:,0]
coordinates = sample[:,1:3]
accuracy = sample[:,3]
time = sample[:,4]

#comb_coord=[str(sample[i,1])+str(sample[i,2]) for i in range(10000)]
#print(len(Counter(comb_coord).keys()))
#print(sum(Counter(comb_coord).values()))

#print(Counter(placeID).keys())
#xave = [[iplaceID, np.mean([x for i, x in np.ndenumerate(coordinates[:,0]) if (placeID[i] == iplaceID)])] for iplaceID in Counter(placeID).keys()]
placeIDcoordinates = pandas.DataFrame(sample[:,[1,2,5]]).groupby([2]).mean()
placeID = placeIDcoordinates.axes[0]
print(placeID.astype(int))
placeIDaccuracy1 = np.nan_to_num(pandas.DataFrame(sample[:,[1,2,5]]).groupby([2]).var())
print(placeIDaccuracy1)
#np.random.shuffle(sample)
#training, test = sample[:8,:], sample[8:,:]
