import tensorflow as tf

# height = a * size + b
height = 170
size = 260

a = tf.Variable(0.1)
b = tf.Variable(0.2)

def loss_func():
    # (실제값 - 예측값)^2
    return tf.square(size - ((height*a)+b))


opt = tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(300):
    opt.minimize(loss_func, var_list=[a,b])
    print(a.numpy(), b.numpy())


