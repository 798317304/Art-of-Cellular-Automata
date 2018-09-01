# -*- coding:utf-8 -*-
# This file serves to provide another way to generate CA map data
# for training ANN_Judge.
# It seems that CNN_Generator is not an efficient nor a currently
# viable way. So I would just use normal methods.

import json
import platform
import os

from os import path
proj_path = path.abspath('.')
print('Currently in directory: ' , proj_path)

from Atm import Atm



# Set the rule to determine whether a CA map satisfies requirement
# this rule is to make sure the the graph is a approximately a large black triangle
# in the middle.
def determine(m):
	for i in range(25):
		for j in range(100):
			if not (49-4*i < j < 51+4*i):
				if m[i][j] == '1':
					return False
	if sum([int(m[k][l]) for k in range(20, 30) for l in range(40, 60) ]) == 0:
		return False
	return True

seeds, judgements = [], []

count = 0
NumTrial = 50000  # The number of trial you want to be incorporated
for i in range(int(1.01*NumTrial)):
	a = Atm()
	a.run()
	
	seeds.append([])
	for k in a.ruleNumBry:
		seeds[-1].append(int(k))
	judgements.append(int(determine(a.c)))

	# if i//55 == 0:
	print(i/(int(1.01*NumTrial)))


if platform.platform()[0] == 'W':
	# In adapting the program to Windows I went through a lot of detours and the
	# line below is another way I found to get the path
	# proj_path = os.path.split(os.path.realpath(__file__))[0]
	print(proj_path + '\ANN_Data\Data_2\Training_Seeds.json')
	with open( proj_path + '\ANN_Data\Data_2\Training_Seeds.json' , 'w') as file:
		json.dump(seeds[:NumTrial], file)
	with open(proj_path + '\ANN_Data\Data_2\Training_Judgements.json', 'w') as file:
		json.dump(judgements[:NumTrial], file)
	with open(proj_path + '\ANN_Data\Data_2\Testing_Seeds.json', 'w') as file:
		json.dump(seeds[NumTrial:], file)
	with open(proj_path + '\ANN_Data\Data_2\Testing_Judgements.json', 'w') as file:
		json.dump(judgements[NumTrial:], file)
else:
	with open(proj_path + '/ANN_Data/Data_2/Training_Seeds.json', 'w') as file:
		json.dump(seeds[:NumTrial], file)
	with open(proj_path + '/ANN_Data/Data_2/Training_Judgements.json', 'w') as file:
		json.dump(judgements[:NumTrial], file)
	with open(proj_path + '/ANN_Data/Data_2/Testing_Seeds.json', 'w') as file:
		json.dump(seeds[NumTrial:], file)
	with open(proj_path + '/ANN_Data/Data_2/Testing_Judgements.json', 'w') as file:
		json.dump(judgements[NumTrial:], file)