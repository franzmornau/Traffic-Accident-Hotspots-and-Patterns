import pandas as pd
import numpy as np
import geopandas as gpd

def p1_turn_gj_to_pd(read_path, write_path):
    '''
    - read the original geojson file
    - filter out the rows that don't have geometry data (coordinates)
    - store the coordinats as normal pandas df columns
    - save as cvs
    parameters: path for reading, path for writing
    returns: written row count
    '''
    acc = gpd.read_file(read_path)
    # some rows don't have location data. We can't use them (by now).
    lc = acc[acc['geometry'].notnull()].copy()
    
    lc['longitude'] = lc['geometry'].bounds['minx']
    lc['latitude']  = lc['geometry'].bounds['miny']
    # cast as Pandas DF, while getting rid of the gojson-specific "geometry" column
    df_p = pd.DataFrame(lc.drop(['geometry'],axis=1))

    df_p.to_csv(write_path)
    print('{} rows where dropped, because they had no location data.'.format((len(acc) - len(df_p))))
    print('The written file has {} rows.'.format(len(df_p)))

    return len(df_p)
