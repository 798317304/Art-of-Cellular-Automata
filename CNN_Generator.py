#-*- coding:utf-8 -*-
'''
This file serves to categorize randomly generator CA graphs,
to provide data for ANN_Judge.
The current rule is black triangle in the middle and the other
parts must be whilte

this file uses the latest Keras grammar

Current rule is : complete black triangle in the middle and the other parts
need to be white
'''

import numpy as np
import json

from os import path
proj_path = path.abspath('.')
print('Currently in directory: ' , proj_path)

from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten
from keras.optimizers import Adam
from keras.utils import np_utils

from Atm import Atm


# 得到原始数据，用来训练模型
# Graphs, Result = [], []
# Now first generate data to train my CNN
# for i in range(100):
# 	a1 = Atm()
# 	a1.run()
# 	Graphs.append(a1.c)
# 	a1.show()
# 	like = input('1 for like: ')
# 	like = '1'
# 	Result.append([
# 		int( like == '1'),
# 		int( like == '0' )
# 		])
# print('i'*100)
# print(len(a1.c[0]))

# to save data
# with open(proj_path + '/CNN_Data/Data_1/100Graphs.json', 'w') as file:
# 	json.dump(Graphs, file)
# with open(proj_path + '/CNN_Data/Data_1/100Result.json', 'w') as file:
# 	json.dump(Result, file)




# 训练以及保存模型
# to load file
with open(proj_path + '/CNN_Data/Data_1/100Graphs.json', 'r') as file:
	Graphs = json.load(file)
with open(proj_path + '/CNN_Data/Data_1/100Result.json', 'r') as file:
	Result = json.load(file)

x_train = np.array(Graphs[:80])
x_train = x_train.reshape(-1, 1, 100, 51)
x_test = np.array(Graphs[80:])
x_test = x_test.reshape(-1, 1, 100, 51)
y_train = np.array(Result[:80])
# y_train = np_utils.to_categorical(y_train, num_classes=2)
y_test = np.array(Result[80:])
# y_test = np_utils.to_categorical(y_test, num_classes=2)
# Each graph is 50*100, 80 testing graphs in total

model = Sequential()

model.add(Conv2D(
	filters = 8, # no. of filter
	kernel_size = (10, 5),
	padding = 'same',
	input_shape = (1, 100, 51)
	))
model.add(Activation('relu'))
model.add(MaxPooling2D(
	pool_size = (5,5),
	strides = (3,3),
	padding = 'same'
	))

model.add(Conv2D(5, (10, 5), padding = 'same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (5,5), padding = 'same'))

model.add(Flatten())
model.add(Dense(15))
model.add(Activation('relu'))
model.add(Dense(2))
model.add(Activation('softmax'))

model.compile(optimizer = 'Adam',
	loss = 'categorical_crossentropy',
	metrics = ['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size = 20)

print('testing --- ')
loss, accuracy = model.evaluate(x_test, y_test)
print('lossL ', loss)
print('accuracy: ', accuracy)

model.save(proj_path + '/Models/CNN_Generator_2.h5')





# 根据模型判断：如果符合标准就打印
# model = load_model(proj_path + '/Models/CNN_Generator_2.h5')

mean_diff = []

for i in range(20):
	a_result = model.predict(x_test[i].reshape(-1, 1, 100, 51))
	mean_diff.append([a_result[0][0], a_result[0][1]])
	if a_result[0][1] > a_result[0][0]:
		a.show()
	else:
		print('No..')
		print(a_result)

# To measure how larger is result[1] than result[0], in form of a mean
count = 0
for i in range(len(mean_diff)):
	count += mean_diff[i][1] - mean_diff[i][0]
mean_diff = count/len(mean_diff)

print('mean_diff is: ', mean_diff)

print()
print()
print()

for i in range(20):
	a = Atm()
	a.run()
	a_result = model.predict(np.array([a.c]).reshape(-1, 1, 100, 51))
	if a_result[0][1] - a_result[0][0] <= mean_diff:
		a.show()
	else:
		print('No..')
		print(a_result)

	# if a_result[0][1] > a_result[0][0]:
	# 	a.show()
	# else:
	# 	print('it\'s {}th time, nothing satisfied'.format(i))
	# 	print('result is: ', a_result)


# Test for over-fitting
# with open(proj_path + '/CNN_Data/Data_1/100Graphs.json', 'r') as file:
# 	Graphs = json.load(file)[45]

# a_result = model.predict(Graphs).reshape(-1, 1, 100, 51)
# if a_result[0][1] > a_result[0][0]:

