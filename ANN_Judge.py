#-*- coding:utf-8 -*-
import numpy as np
import random
import json

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import RMSprop

with open('/Users/huqitian/Desktop/200Feature.json', 'r') as file:
	x_train = np.array(json.load(file))
with open('/Users/huqitian/Desktop/200Judgement2.json', 'r') as file:
	y_train = np.array(json.load(file))
with open('/Users/huqitian/Desktop/30Feature.json', 'r') as file:
	x_test = np.array(json.load(file))
with open('/Users/huqitian/Desktop/30Judgement.json', 'r') as file:
	y_test = np.array(json.load(file))



model = Sequential([
	Dense(62, input_dim = 31), # 32 is output_dim
	Activation('relu'),
	Dropout(0.7),
	Dense(31),
	Activation('relu'),
	# Dropout(0.5),
	Dense(2), # 输出10个份额里
	# Activation('softmax')
	])

model.compile(
	optimizer='rmsprop',
	loss = 'categorical_crossentropy',
	metrics = ['accuracy'], # 同时计算准确率
	)

# print('Training...')
model.fit(x_train, y_train, nb_epoch=10, batch_size=10) 

loss, accuracy = model.evaluate(x_test, y_test)


print('test loss', loss)
print('test accuracy', accuracy)






