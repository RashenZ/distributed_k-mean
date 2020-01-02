#!/bin/bash/python

import time
import sys
import os
import random

class DistributedKMeans:
	"""docstring for DistributedKMeans"""
	def __init__(self,
			Xm = {"0": [1, 2, 3, 15], "1": [2, 2, 5, 1], "2": [4, 3, 10, 50]},
			M = 5,
			K = 3,
			Nm = 10,
			T = 5
			):
		self.Xm = Xm # Set of all observation of not m {nodex: [observation1, observation2]}
		self.M = M # Number of node
		self.K = K # Number of cluster
		self.Nm = Nm # Number of observation of node m
		self.T = T # Number max of iteration
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
		# print("center C = ")
		# print(self.C)
		# print("SSE = ")
		# print(self.SSEList)

		for SSE in self.SSEList:
			for value in self.SSEList[SSE]:
				if value >= 20:
					print("TO SPLIT")
					self.splitCluster(SSE)
					break

	def splitCluster(self, cluster):
		""" split the cluster in 2 sub cluster """
		maxValue = self.getMaxValue(self.clusterList[cluster])
		minValue = self.getMinValue(self.clusterList[cluster])
		midValue = round(maxValue - ((maxValue - minValue) / 2))

		# Create a set of centroid
		firstCentroid = random.randint(minValue, midValue)
		secondCentroid = random.randint(midValue, maxValue)

		cpyCluster = self.clusterList[cluster]
		nextName = str(len(self.clusterList))
		self.clusterList[cluster] = []
		self.clusterList[nextName] = []

		for value in cpyCluster:
			if abs(value - firstCentroid) < abs(value - secondCentroid):
				self.clusterList[cluster].append(value)
			else:
				self.clusterList[nextName].append(value)
			pass
		pass
		print(self.clusterList)


	def average_consensus(self, cluster):
		""" Calculate the average consensus sum(value of cluster) / len(cluster) """
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
		for index, observation in enumerate(cluster):
			SSE.append(abs(observation - center))

		# return Sum of all (observation - center) squared
		return SSE

	def start(self):
		""" start distributed k-means loop """
		self.distributedVarPart()
		while self.t < self.T:
			self.t += 1
			for cluster in self.clusterList:
				print("cluster: ")
				print(cluster)
				print(self.clusterList[cluster])
				self.C[cluster] = self.average_consensus(self.clusterList[cluster])
			print(self.C)
			print("turn t=%s: Centroids%s"% (self.t, self.C), flush=True)
			time.sleep(1)
