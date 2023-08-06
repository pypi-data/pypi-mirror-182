import tensorflow as tf
import numpy as np
from tfe.initializers import HeUniform

class Conv2D(tf.keras.layers.Layer):
  
  def __init__(self,
               filters,
               kernel_size,
               strides = (1, 1),
               padding = "valid",
               data_format = None,
               dilation_rate = (1, 1),
               groups = 1,
               activation = None,
               use_bias = True,
               kernel_initializer = None,
               bias_initializer = "zeros",
               kernel_regularizer = None,
               bias_regularizer = None,
               activity_regularizer = None,
               kernel_constraint = None,
               bias_constraint = None,
               **kwargs
              ):
    super(Conv2D, self).__init__()
    
    if kernel_initializer is None:
      kernel_initializer = HeUniform(np.sqrt(5),
                                     "fan_in",
                                     "leaky_relu")
      
    self.torch_padding = None
    if isinstance(padding, list) or isinstance(padding, tuple):
      self.torch_padding = padding
      padding = "valid"
      
    self.conv2d = tf.keras.layers.Conv2D(filters = filters,
                                         kernel_size = kernel_size,
                                         strides = strides,
                                         padding = padding,
                                         data_format = data_format,
                                         dilation_rate = dilation_rate,
                                         groups = groups,
                                         activation = activation,
                                         use_bias = use_bias,
                                         kernel_initializer = kernel_initializer,
                                         bias_initializer = bias_initializer,
                                         kernel_regularizer = kernel_regularizer,
                                         bias_regularizer = bias_regularizer,
                                         activity_regularizer = activity_regularizer,
                                         kernel_constraint = kernel_constraint,
                                         bias_constraint = bias_constraint,
                                         **kwargs
                                        )
    
  def call(self, inputs):
    if self.torch_padding:
      inputs = tf.pad(inputs,
                      [[0, 0],
                      [self.torch_padding[0], self.torch_padding[0]],
                      [self.torch_padding[1], self.torch_padding[1]],
                      [0, 0]],
                      "CONSTANT")
    out = self.conv2d(inputs)
    return out