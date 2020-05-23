import tensorflow_datasets as tfds
from abc import ABC, abstractmethod

class Encoder(object):
    def __init__(self):
        self.encoder = tfds.features.text.TokenTextEncoder([])
        
    @abstractmethod
    def to_id(self, path):
        pass
    
    def save(self, path):
        self.encoder.save_to_file(path)
    
    def load(self, path):
        self.encoder = tfds.features.text.TokenTextEncoder.load_from_file(path)
        
    def encode(self, s):
        return self.encoder.encode(s)
    
    def decode(self, idx):
        return self.encoder.decode(idx)
    
class NodeEncoder(Encoder):    
    def to_id(self, triplet):
        nodes = pd.concat([triplet["head"], triplet["tail"]]).unique().tolist()
        self.encoder = tfds.features.text.TokenTextEncoder(nodes)
        
class EdgeEncoder(Encoder):
    def to_id(self, triplet):
        edges = triplet["rel"].unique().tolist()
        self.encoder = tfds.features.text.TokenTextEncoder(edges)