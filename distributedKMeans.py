#!/bin/bash/python

import time
import sys
import os
import random

class DistributedKMeans:
	"""docstring for DistributedKMeans"""
	def __init__(self):
		self.Xm = {"0": [1, 2, 3], "1": [2, 2, 5], "2": [4, 3, 10]} # Set of all observation of not m {nodex: [observation1, observation2]}
		self.M = 5 # Number of node
		self.K = 3 # Number of cluster
		self.Nm = 10 # Number of observation of node m
		self.t = 0 # Iteration
		# self.centroid = []
		# self.nodesDict = {}

	def getMinValue(self, cluster):
		minValue = 0
		print(cluster)
		for index, value in enumerate(cluster):
			if index == 0:
				minValue = value
			elif value < minValue:
				minValue = value
		return minValue

	def getMaxValue(self, cluster):
		maxValue = 0
		for index, value in enumerate(cluster):
			if index == 0:
				maxValue = value
			elif value > maxValue:
				maxValue = value
		return maxValue

	def distributedVarPart(self):
		""" initialize the cluster """
		self.C = [] # Center of all cluster k
		self.clusterList = {} # List of all cluster with observations
		self.SSEList = {} # List of SSE of cluster k

		# initialize cluster
		for node in self.Xm:
			for index, observation in enumerate(self.Xm[node]):
				if index not in self.clusterList:
					self.clusterList[index] = []
				self.clusterList[index].append(observation)
		print(self.clusterList)

		# set the center (centroid) of k (random for the first iteration) and calculate and set the SSE 
		for index, cluster in enumerate(self.clusterList):
			self.C.append(random.randint(self.getMinValue(self.clusterList[cluster]), self.getMaxValue(self.clusterList[cluster])))
			self.SSEList[cluster] = self.calculateSSE(self.clusterList[cluster], self.C[index])
		print("center C = ")
		print(self.C)
		print("SSE = ")
		print(self.SSEList)


	def average_consensus(self, cluster):
		""" Calculate the average consensus """
		centerk = 0
		index = 0
		for value in cluster:
			centerk += value
			index += 1
		centerk = centerk / index
		return centerk

	def calculateSSE(self, cluster, center):
		""" calculate the Error Sum of Squares (SSE) for each cluster """
		SSE = []
		print("toto")
		print(self.C)
		for index, observation in enumerate(cluster):
			SSE.append(abs(observation - center))

		# return Sum of all (observation - center) squared
		print(SSE)
		return SSE
		pass




	def start(self):
		""" start distributed k-means loop """
		self.distributedVarPart()
		while self.t < 3:
			self.t += 1
			print(self.t, flush=True)
			time.sleep(1)
