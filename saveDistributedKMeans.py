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
		# self.t = 0 # Iteration
		# self.centroid = []
		# self.nodesDict = {}

	def initialize(self, dirPath="./Files"):
		""" initialize everything we need befire we start the loop.
			In this case we initialize the data we need
			in order to create the cluster and iterate with the value
		"""
		filesList = os.listdir(dirPath)
		for file in filesList:
			self.nodesDict[file] = {}
			with open(dirPath + "/" + file, 'r') as fd:
				line = fd.readline()
				while line:
					observation = line.split(":")[0]
					values = line.split(":")[1].split(";")
					self.nodesDict[file][observation] = values
					line = fd.readline()
		print(self.nodesDict)
		self.setCentroid()
		pass

	def updateCentroid(self):
		""" Update the centroid during iteration """
		pass

	def updateClusters(self):
		""" Update clusters during iteration """
		pass

	def setClusters(self):
		""" Set clusters for the first iteration """
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
		while self.n < self.M:
			self.n += 1
			print(self.n, flush=True)
			time.sleep(1)
