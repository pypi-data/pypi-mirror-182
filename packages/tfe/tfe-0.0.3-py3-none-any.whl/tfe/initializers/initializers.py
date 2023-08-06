import tensorflow as tf
import numpy as np

class HeUniform(tf.keras.initializers.Initializer):
  
  def __init__(self, a, mode, nonlinearity, bound = None):
    self.a = a
    self.mode = mode
    self.nonlinearity = nonlinearity
    self.bound = bound
    
    if self.nonlinearity == "sigmoid":
      self.gain = 1
    elif self.nonlinearity == "tanh":
      self.gain = 5.0 / 3
    elif self.nonlinearity == "relu":
      self.gain = np.sqrt(2.0)
    elif self.nonlinearity == "leaky_relu":
      if self.a is None:
        self.gain = .01
      else:
        self.gain = np.sqrt(2.0 / (1 + self.a ** 2))
    elif self.nonlinearity == "selu":
      self.gain = 3.0 / 4
    
  def __call__(self, shape, dtype = None, **kwargs):
    if self.bound:
      return tf.random.uniform(shape,
                               minval = -self.bound,
                               maxval = self.bound)
    
    torch_shape = np.flip(shape)
    
    num_input_fmaps = torch_shape[1]
    num_output_fmaps = torch_shape[0]
    receptive_field_size = 1
    if len(torch_shape) > 2:
      for s in torch_shape[2:]:
        receptive_field_size *= s
    fan_in = num_input_fmaps * receptive_field_size    
    fan_out = num_output_fmaps * receptive_field_size
    
    if self.mode == "fan_in":
      fan = fan_in
    elif self.mode == "fan_out":
      fan = fan_out
      
    std = self.gain / np.sqrt(fan)
    bound = np.sqrt(3.0) * std
    
    return tf.random.uniform(shape,
                             minval = -bound,
                             maxval = bound)