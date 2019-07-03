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

    def get_all_coll(self):
        '''
        get the full dataframe
        Paramteters: none
        returns: Pandas DF
        '''
        return self._original_acc_data.copy()
    
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
        
        X = self._original_acc_data
        X_pmvc = X[X['SDOT_COLDESC'].isin(pmvc)].copy()

        return X_pmvc