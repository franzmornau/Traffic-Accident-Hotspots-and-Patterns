import pandas as pd

class Acc_data:
    ''' 
    - read accident data from the Seattle source
    - further cleaning
    - provide slices from it
    (to be further enhanced, with bicyle accident data, pedestrians, etc.)
    '''
    def __init__(self, file_path):   
        self._original_acc_data = pd.read_csv(file_path, low_memory=False)
        self.acc_data_cl1 = self._get_coll_cl1()

    def _get_coll_cl1(self):
        ''' cleaning stage 1
        - make sure SDOT_COLDESC is filled
        - remove 2003 (just 1 DS, blurring the timeline)
        '''
        X = self._original_acc_data
        X = X[X['year'] != 2003]
        # just a band aid for now, should be taken care of when reading: 
        X['ds']=X.ds.apply(lambda x: pd.to_datetime(x))
        return X[X['SDOT_COLDESC'].notnull()]

    def get_coll_data_uncleaned(self):
        '''
        get the full dataframe
        Paramteters: none
        returns: Pandas DF
        '''
        return self._original_acc_data.copy()

    def get_cleaned_coll(self):
        '''
        get the full dataframe
        Paramteters: none
        returns: Pandas DF
        '''
        return self.acc_data_cl1.copy()
    
    def get_pure_mv_coll(self):
        '''
        delivers DF with only the collisions between motor vehicles
        Paramteters: none
        returns: Pandas DF
        '''
        pmvc =['MOTOR VEHICLE STRUCK MOTOR VEHICLE, FRONT END AT ANGLE',
                'MOTOR VEHICLE STRUCK MOTOR VEHICLE, REAR END',
                'MOTOR VEHICLE STRUCK MOTOR VEHICLE, LEFT SIDE SIDESWIPE',
                'MOTOR VEHICLE STRUCK MOTOR VEHICLE, LEFT SIDE AT ANGLE',
                'MOTOR VEHICLE STRUCK MOTOR VEHICLE, RIGHT SIDE SIDESWIPE',
                'MOTOR VEHICLE STRUCK MOTOR VEHICLE, RIGHT SIDE AT ANGLE']
        
        X = self.acc_data_cl1
        X_pmvc = X[X['SDOT_COLDESC'].isin(pmvc)].copy()

        return X_pmvc

    def get_cyclist_coll(self):
        '''
        delivers DF with only the collisions that include a pedalcyclist
        Paramteters: none
        returns: Pandas DF
        '''   
        X = self.acc_data_cl1
        X_cyc = X[X['SDOT_COLDESC'].str.contains('PEDALCYCLIST')].copy()

        return X_cyc

    def get_pedestrian_coll(self):   
        '''
        delivers DF with only the collisions that include a pedestrian
        Paramteters: none
        returns: Pandas DF
        '''        
        X = self.acc_data_cl1
        X_ped = X[X['SDOT_COLDESC'].str.contains('PEDESTRIAN')].copy()

        return X_ped

    def get_weekly_data_cw(self,start_year=2004,end_year=2019):
        '''
        Get data aggregated by calendar week.
        beware: this messes with the numbers around year change.
        Paramteters: start_year, end year: int in [2004, 2019]
        Returns: Pandas DF
        '''
        X = self.acc_data_cl1.copy()
        X = X[(X['year'] >= start_year) & (X['year'] <= end_year)]
        X_w = X[['year','week','OBJECTID']].groupby(['year','week']).count()
        X_wh = X[['year','week','is_holiday']].groupby(['year','week']).max()
        X_wh.rename({'is_holiday': 'has_holiday'}, axis=1, inplace=True)
        X_w = X_w.join(X_wh)     

        week_numbers = X_w.reset_index()
        week_numbers.rename({'OBJECTID': 'acc_nr'}, axis=1, inplace=True)

        week_means=week_numbers[['week','acc_nr']].groupby(['week']).mean()
        week_numbers['week_mean']=week_numbers.week.apply(lambda x: week_means['acc_nr'][x])
        return week_numbers

    def get_weekly_cw_dummyfied(self,start_year=2004,end_year=2019):
        '''
        Get data aggregated by calendar week.
        beware: this messes with the numbers around year change (cws 1 / 52 /53).
        Paramteters: start_year, end year: int in [2004, 2019]
        Returns: Pandas DF
        '''
        week_numbers = self.get_weekly_data_cw(start_year,end_year)
        week_d = pd.get_dummies(week_numbers.week).join(week_numbers)
        week_d['year_red']= week_d.year.apply(lambda x: x-2004)
        week_d.drop(['week','year'], axis=1, inplace=True)
        return week_d