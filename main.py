#!/bin/bash/python

from distributedKMeans import DistributedKMeans

if __name__ == '__main__':
	print("hello")
	KMeans = DistributedKMeans()
	KMeans.start()