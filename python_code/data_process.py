import numpy as np
import pandas as pd

'''
gps = pd.read_csv('F:/CodeWorkspace/VueCliWorkspace/holmes-eyes/static/data/raw_data/gps.csv')

for index,item in gps.groupby('id'):
    item.to_csv('../static/data/gps/' + str(index) + '.csv',index=False)
'''

credits = pd.read_csv('F:/CodeWorkspace/VueCliWorkspace/holmes-eyes/static/data/raw_data/cc_data.csv')


print(credits)
