import tensorflow as tf

tensor1 = tf.constant( [3,4,5] )
tensor2 = tf.constant( [6,7,8] )

tensor3 = tf.constant([ [1, 2], 
                        [3, 4] ])

w = tf.Variable(1.0)
w.assign(2)
print(w.numpy())