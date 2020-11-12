import keras                                                                                
import keras.backend as K

class onehot_pdgid:
    def __call__(self,x):
        return K.one_hot(K.cast(K.abs(x) > 11 , "int32"),2)
    @property
    def add_dim(self):
        return 1
class onehot_charge:
    def __call__(self,x):
        return K.one_hot(K.cast(x > 0 , "int32"),2)
    @property
    def add_dim(self):
        return 1
class onehot_era:
    def __call__(self,x):
        return K.one_hot(K.cast(x - 2016 , "int32"),3)
    @property
    def add_dim(self):
        return 2
class onehot_unit:
    def __call__(self,x):
        return K.expand_dims(x,1)
    @property
    def add_dim(self):
        return 0


class OneHot(keras.layers.Layer):
    def __init__(self,onehots,**kwargs):
        super(OneHot, self).__init__(**kwargs)
        self.onehots = onehots 
    def call(self,x):
        out = [self.onehots[i](x[:,i]) for i in range(x.shape[1])]
        return K.concatenate(out,axis=1)                                                    
    def compute_output_shape(self,input_shape):
        add_dims = sum([onehot.add_dim for onehot in self.onehots])
        return (input_shape[0],input_shape[1]+add_dims)
    def get_config(self):
        config = super(OneHot, self).get_config()
        config['onehots'] = [type(onehot).__name__ for onehot in self.onehots]
        return config
    @classmethod
    def from_config(cls,config):
        config['onehots'] = [globals()[onehot]() for onehot in config['onehots']]
        return cls(**config)
