#-*- coding:utf-8 -*-

import random
from collections import defaultdict

class atm():
	# r = 2, k = 2

	RULE_NUMBER = random.randint(100000000, 2147483647)

	def __init__(self, ruleNumDec = RULE_NUMBER, d = 100): 
		# rng is the range, d is size of map

		# get number of rule, in decimal
		# ruleNumDec = input("Which rule do you want to use? (0 ~ 2147483647) ")
		while not(0 <= int(ruleNumDec) & int(ruleNumDec) < 2147483648):
			print("out of range!")
			ruleNumDec = input("Which rule do you want to use? (0~2147483648) ")

		ruleNumBry = bin(int(ruleNumDec))[2:].zfill(31) # This is a string
		self.ruleNumBry = ruleNumBry
		# print(ruleNumBry)

		self.rule = defaultdict(int)
		for i in range(31):
			self.rule[bin(i)[2:].zfill(5)] = ruleNumBry[i]
			# print(i)

		# setting up initial map
		self.d = d # int(input("Range of the map: "))
		self.a, self.b = [], [] # a, b are two maps

		for i in range(d): # initialize with 0, and 1 in the middle one box
			self.a.append("0") 
			self.b.append("0")
		self.a[d//2], self.b[d//2] = "1", "1"

	def run(self):
		# print the first round 
		for i in range(self.d):
			if self.b[i] == "1":
				print("██", end = "")
			else:
				print("  ", end = "")

		print()

		# doing calculation and printing 
		for count in range(30):
			for i in range(self.d):
				group = str(self.a[i-2]) + str(self.a[i-1]) + str(self.a[i]) + str(self.a[(i+1+self.d)%self.d]) + str(self.a[(i+2+self.d)%self.d])
				self.b[i] = self.rule[group]
				if self.b[i] == "1":
					print("██", end = "")
				else:
					print("  ", end = "")
			self.a = self.b.copy()
			print()
			# input()
	
	def response(self, re = True):
		self.re = int(input('1: like, 0: dislike'))
		return self.re



a1 = atm()
a1.run()
print(a1.ruleNumBry)