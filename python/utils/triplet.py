import pandas as pd

class Triplet(object):
    def __init__(self, path, **kwargs):
        self.df = pd.read_csv(path, **kwargs)
    
    def __getitem__(self, key):
        return self.df[key]