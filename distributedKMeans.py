#!/bin/bash/python

import time
import sys
import os

class DistributedKMeans:
	"""docstring for DistributedKMeans"""
	def __init__(self):
		self.Xm = [] # Set of all observation of not m
		self.M = 5 # Number of node
		self.K = 3 # Number of cluster
		self.Nm = 10 # Number of observation of node m
		self.t = 0 # Iteration
		# self.centroid = []
		# self.nodesDict = {}

	def distributedVarPart(self):
		""" initialize the cluster """
		self.C = [] # Center of all cluster k
		for cluster in range(1, self.K):
			print("cluster: " + str(cluster))
			SSE = self.calculateSSE()
			pass
		pass

	def average-consensus(self, SSEm):

		pass

	def calculateSSE(self):
		""" calculate the Error Sum of Squares (SSE) for each cluster """
		return SSE
		pass

	def setCentroid(self):
		""" Set the centroid for the first iteration """
		tmpObsDico = {}
		for node in self.nodesDict:
			for observation in self.nodesDict[node]:
				if observation not in tmpObsDico:
					tmpObsDico[observation] = []
				tmpObsDico[observation].append(self.nodesDict[node][observation][self.t])
		print("\n")
		print(tmpObsDico)
				
		pass

	def start(self):
		""" start distributed k-means loop """
		self.distributedVarPart()
		while self.t < 3:
			self.t += 1
			print(self.t, flush=True)
			time.sleep(1)
