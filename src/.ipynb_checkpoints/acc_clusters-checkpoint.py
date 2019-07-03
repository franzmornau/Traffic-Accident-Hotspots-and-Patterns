import pandas as pd
import geopandas as gpd
import numpy as np
import itertools

import scipy.stats as stats
from sklearn.cluster import DBSCAN

class Ac_cluster:
    ''' 
    - hold accident data from the Seattle source
    - provide slices from it
    - provide cluster data
    '''
    def __init__(self, accident_df, sel_size=2000, eps=0.001, min_samples=5):
        '''
        Parameters: 
        - Pandas DataFrame with coordinates as 'logitude', 'latitude'
        - integer selection size on which to work on
        '''
        self.sel_size = min(sel_size,len(accident_df))
        self.accident_data = accident_df
        self.X = np.array(self.accident_data[['longitude','latitude']])
        x = self.X[:sel_size]
        self.clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(x)
        self.labels = self.clustering.labels_
        self.labels_count = len(np.unique(self.labels))
        
        self.labels_clustered = self.labels[self.labels!=-1]
        self.points_clustered = x[self.labels != -1, :]
        
        self.dfx = pd.DataFrame(self.points_clustered, columns=['longitude', 'latitude'])
        self.dfx['cluster'] = self.labels_clustered
        
        self.cluster_counts = self.dfx.groupby('cluster').count()[['longitude']]\
            .sort_values('longitude',ascending=False)
        self.cluster_counts.rename(index=int, columns={'longitude': 'point'}, inplace=True)

        self.nr_of_clusters = len(self.cluster_counts)

    def get_clusters_head(self, nr_of_cl=5):
        ''' 
        - get the first nr_of_cl clusters in the list, ordered by cluster size.
        (So, this gets you the n heaviest clusters, n = nr_of_cl (or just all of them 
        if nr_of_cl is bigger than the number of clusters in the sample).)
        '''
        n = min(nr_of_cl,self.nr_of_clusters)
        cl_head = self.cluster_counts.head(n).index
        
        mask = np.isin(self.labels_clustered, cl_head)
        l_c = self.labels_clustered[mask]
        x_c = self.points_clustered[mask, :]
        
        return x_c, l_c
