class TripletEmbedding(tf.keras.layers.Layer):
    def __init__(self, 
                 node_num, 
                 edge_num, 
                 emb_dim,
                 embeddings_initializer='uniform',
                 embeddings_regularizer=None, 
                 activity_regularizer=None,
                 embeddings_constraint=None, 
                 mask_zero=False, 
                 input_length=None, 
                 **kwargs):
        
        dtype = kwargs.pop('dtype', K.floatx())
        # We set autocast to False, as we do not want to cast floating- point inputs
        # to self.dtype. In call(), we cast to int32, and casting to self.dtype
        # before casting to int32 might cause the int32 values to be different due
        # to a loss of precision.
        kwargs['autocast'] = False
        super(TripletEmbedding, self).__init__(dtype=dtype, **kwargs)
        
        self.node_emb = tf.keras.layers.Embedding(node_num, 
                                                  emb_dim, 
                                                  embeddings_initializer, 
                                                  embeddings_regularizer, 
                                                  activity_regularizer,
                                                  embeddings_constraint,
                                                  mask_zero,
                                                  input_length,
                                                  **kwargs)
        
        self.edge_emb = tf.keras.layers.Embedding(edge_num, 
                                                  emb_dim, 
                                                  embeddings_initializer, 
                                                  embeddings_regularizer, 
                                                  activity_regularizer,
                                                  embeddings_constraint,
                                                  mask_zero,
                                                  input_length,
                                                  **kwargs)
        
        self.edge_num = edge_num
        self.node_num = node_num
        
    def build(self, input_shape):
        self.node_emb.build(input_shape)
        self.edge_emb.build(input_shape)
    
    def call(self, inputs):
        h_pos, r_pos, t_pos = self.node_emb.call(x[:, 0]), self.edge_emb.call(x[:, 1]), self.node_emb.call(x[:, 2])
        
        neg_size = h_pos.shape[0]
        h_neg_idx = tf.random.uniform((neg_size, ), minval=0, maxval=self.node_num, dtype=tf.int32)
        r_neg_idx = tf.random.uniform((neg_size, ), minval=0, maxval=self.edge_num, dtype=tf.int32)
        t_neg_idx = tf.random.uniform((neg_size, ), minval=0, maxval=self.node_num, dtype=tf.int32)
        
        # WRONG
        h_neg, r_neg, t_neg = self.node_emb.call(h_neg_idx), self.edge_emb.call(r_neg_idx), self.node_emb.call(t_neg_idx)
        
        y_pos = h_pos + r_pos - t_pos
        y_neg = h_neg + r_neg - t_neg
        
        return tf.stack([y_pos, y_neg], axis = 1)