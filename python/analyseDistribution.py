import collections
import matplotlib.pyplot as plt
import numpy
""" Read in the Mallet output file and analyse the topic distribution"""


dist = open('../Mallet/documentTopics.txt').readlines()

paperDist = collections.defaultdict(list)
for line in dist:
	line=line.split()
	doc = line[1].split('/')[-1]
	paper = doc.split('_')[0]
	print paperDist.keys()
	paperDist[paper] = [float(n) for n in line[2:]]

rightPapers = ['Mail', 'The Mail on Sunday','Express','Telegraph', 'The Sunday Telegraph']
leftPapers = ['Guardian','Independent', 'Independent On Sunday', 'The Observer']
centrePapers = ['FT', 'Times']
keepPapers = rightPapers+leftPapers+centrePapers


cultureVals=collections.defaultdict(list)
econVals=collections.defaultdict(list)
for k in keepPapers:
	print k
	print paperDist[k][0]
	print cultureVals[k]





	cultureVals[k].append(paperDist[k][0])
	econVals[k].append(paperDist[k][6])

#print cultureVals
#print keepPapers

paperNames =[]
meanValues =[] 
for x in keepPapers:
	paperNames.append(x)
	meanValues.append(numpy.mean(cultureVals[x]))
plt.bar(range(len(keepPapers)), meanValues, align="center")
#plt.suptitle("Topic 0: Identity/Education")
plt.suptitle("Topic 6: Economy")
plt.xticks(range(len(keepPapers)), keepPapers)
plt.show()