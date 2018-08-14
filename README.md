# CellularAutomata-NeuralNetwork
## Introduction
Use neural network, based on user or CNN generated data, to determine whether one graph of CA will be liked. It is firstly an attempt to use NN to understand a chaos system, and secondly an attempt to simulate human aesthetics with algorithm.
## Structure of project
* ANN_Judge.py uses artificial neural network to judge whether one particular CA graph satisfies user's standard.
* atm.py is 1D cellular automata with r = 2, k = 2.
* User_data_collection.py use atm.py to make it easy for users to generate preference data.
* CNN_Generator.py uses convolutional neural network to judge whether a CA picture satisfies user-induced standard. This now serves to provide data for ANN_Judge, because now it cannot understand the relation between a CA seed (in my case a 31-digit binary number) and features of its graph.
