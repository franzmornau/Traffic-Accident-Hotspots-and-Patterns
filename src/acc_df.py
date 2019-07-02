    class Acc_data:
    ''' 
    *STILL A STUBB, UNCLEAR IF NEEDED AT ALL*
    - read accident data from the Seattle source
    - further cleaning
    - provide slices from it
    '''
    def __init__(self,data_path):   
        self.original_acc_data = pd.read_csv(data_path, low_memory=False