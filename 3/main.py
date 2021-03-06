import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

import tensorflow_hub as hub
import tensorflow_datasets as tfds

print('version: ',tf.__version__)
print('inst exec mode: ',tf.executing_eagerly())
print('hub ver: ', hub.__version__)
print('GPU: ','ENABLE' if tf.config.experimental.list_physical_devices('GPU') else 'DISABLE')

train_data, validation_data, test_data = tfds.load(name='imdb_reviews',
                                                   split=('train[:60%]', 'train[60%:]', 'test'),
                                                   as_supervised=True)

train_examples_batch, train_labels_batch = next(iter(train_data.batch(10)))
print(train_examples_batch)
print(train_labels_batch)

embedding = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
hub_layer = hub.KerasLayer(embedding,input_shape=[],dtype=tf.string,trainable=True)

hub_layer(train_examples_batch[:3])

model = tf.keras.Sequential()
model.add(hub_layer)
model.add(tf.keras.layers.Dense(16,activation='relu'))
model.add(tf.keras.layers.Dense(1))

model.summary()
