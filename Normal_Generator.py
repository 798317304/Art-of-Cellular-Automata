#-*- coding:utf-8 -*-
# This file serves to provide another way to generate CA map data
# for training ANN_Judge.
# It seems that CNN_Generator is not an efficient nor a currently
# viable way. So I would just use normal methods.

import numpy as np
import json

from os import path
proj_path = path.abspath('.')
print('Currently in directory: ' , proj_path)

from Atm import Atm



# Set the rule to determine whether a CA map satisfies requirement
# this rule is to make sure the the graph is a appriximately a large black triangle
# in the middle.
def determine(m):
	for i in range(25):
		for j in range(100):
			if not (j > 49-4*i and j < 51+4*i):
				if m[i][j] == '1':
					return False
	if sum([ int(m[i][j]) for i in range(20, 30) for j in range(40, 60) ]) == 0:
		return False
	return True

seeds, judgements = [], []

count = 0
for i in range(55000):
	a = Atm()
	a.run()
	
	seeds.append([])
	for k in a.ruleNumBry:
		seeds[-1].append(int(k))
	judgements.append(int(determine(a.c)))

	# if i//55 == 0:
	print(i/55000)


with open(proj_path + '/CNN_Data/Data_2/Training_Seeds.json', 'w') as file:
	json.dump(seeds[:50000], file)
with open(proj_path + '/CNN_Data/Data_2/Training_Judgements.json', 'w') as file:
	json.dump(judgements[:50000], file)
with open(proj_path + '/CNN_Data/Data_2/Testing_Seeds.json', 'w') as file:
	json.dump(seeds[50000:], file)
with open(proj_path + '/CNN_Data/Data_2/Testing_Judgements.json', 'w') as file:
	json.dump(judgements[50000:], file)





