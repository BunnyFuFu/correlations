import numpy as np
import pylab as pl

def readFile(filename):
	"""puts file data into 3D array"""

def getTimeRange(a):
	x, y, z = a.shape
	return range(x-1)

def arrayCorr(a, time):
	"""returns list of correlations given a 3D array"""
	corr = [(np.abs(a[i] - a[i+1])**2).flatten().mean() for i in time]
	return corr

def overallCorr(data, time):
	"""returns list of  correlations of entire sample"""
	dataArray = np.asarray(data)
	corr = [dataArray[:,i].mean() for i in time]
	return corr
	
def generateIndivGraph(a):
	"""plots correlation vs change in time 
	given one 3D array
	"""
	timeRange = range(len(a))
	pl.plot(timeRange, arrayCorr(a, timeRange)) 

def generateOverallGraph(a):
	"""Plots correlation vs change in time"""
	
	timeRange = range(len(a))
	pl.plot(timeRange, a) 

