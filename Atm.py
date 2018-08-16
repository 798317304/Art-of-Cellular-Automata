#-*- coding:utf-8 -*-
'''
This edition of automata is supposed to be more OOP.
Setup, reset, run, and attributes more clearly defined.
in run a printable c is generated, but no printing conducted.
print is another function
The aim is to get rid of re-writing this class in other files,
but to use import.

'''

'''

潜在的问题：range 31？ 这些数量对的上不？

'''


import random
from collections import defaultdict



class Atm():
	# r = 2, k = 2


	def __init__(self, ruleNumDec = 0, dim = 100): 
		# rng is the range, d is size of map

		if not ruleNumDec:
			ruleNumDec = random.randint(0, 2147483647)

		# get number of rule, in decimal
		# ruleNumDec = input("Which rule do you want to use? (0 ~ 2147483647) ")
		while not(0 <= int(ruleNumDec) & int(ruleNumDec) < 2147483648):
			print("out of range!")
			ruleNumDec = input("Which rule do you want to use? (0~2147483648) ")

		self.ruleNumBry = bin(int(ruleNumDec))[2:].zfill(31) # This is a string

		self.rule = defaultdict(int)
		for i in range(31):
			self.rule[bin(i)[2:].zfill(5)] = self.ruleNumBry[i]
			# print(i)

		# setting up initial map
		self.dim  = dim # int(input("Range of the map: "))
		self.a, self.b = [], [] 
		# a, b are two maps. a is intermediary, b is each printable row

		for i in range(self.dim): # initialize with 0, and 1 in the middle one box
			self.b.append("0")
			self.a.append("0")
		self.b[self.dim//2], self.a[self.dim//2] = "1", "1"


	def run(self, time = 50): # is to generate c, a printable 2-D list
		# b is the 1-D map: each row to be printed
		# c is the comprehensive 2-D map, with dimension time*d
		self.c = [[]]
		for i in range(self.dim): # initialize with 0, and 1 in the middle one box
			self.c[0].append("0")
		self.c[0][self.dim//2] = "1"


		# copy the first row
		# print the first round 

		# doing calculation and printing 
		for count in range(time):
			for i in range(self.dim):

				group = str(self.a[i-2]) +\
				str(self.a[i-1]) +\
				str(self.a[i]) +\
				str(self.a[(i+1+self.dim)%self.dim])+\
				str(self.a[(i+2+self.dim)%self.dim])

				self.b[i] = self.rule[group]
			self.a = self.b.copy()
			self.c.append(self.b.copy())
	
	def show(self): # show the result of 
		for i in self.c:
			for j in i:
				if j == '1':
					print("██", end = "")
				if j == '0':
					print("  ", end = "")
			print()

# 用来debug的
# def smartPrint(a):
# 		for j in a:
# 			if j == '1':
# 				print("██", end = "")
# 			if j == '0':
# 				print("  ", end = "")
# 		print()




# a1 = atm()
# a1.run(3)
# a1.show()
# print(a1.ruleNumBry)
