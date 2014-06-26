import collections
import matplotlib.pyplot as plt
import numpy
import sys
""" Read in the Mallet output file and analyse the topic distribution"""



"""initialize mappings of papers, days and weeks to posterior
document topic distributions"""
def read_dist(dist):

	paperDist = collections.defaultdict(list)
	dayDist = collections.defaultdict(list)
	weekDist = collections.defaultdict(list)
	for line in dist:
		line=line.split()
		doc = line[1].split('/')[-1]
		paper = doc.split('_')[0]
		day = doc.split('_')[1]
		week = str(int(day)/7)
		dayDist[day].append([float(n) for n in line[2:]])
		weekDist[week].append([float(n) for n in line[2:]])
		paperDist[paper].append([float(n) for n in line[2:]])
	return(paperDist, dayDist, weekDist)



rightPapers = ['telegraph', 'mail', 'express']
leftPapers = ['independent','guardian']
centrePapers = [ 'sun', 'times', 'ft']
papers = leftPapers+centrePapers+rightPapers
days = [str(d) for d in range(45,180)]
weeks = [str(d) for d in range(7,21)]



def topic_per_attribute(topic, attribute,attDist):
	topicByAttribute  = collections.defaultdict(list)
	meanValues=[]
	for a in attribute:
		topicVals=[]
		if a in attDist.keys() and len(attDist[a]) > 5:
			thisAtt = attDist[a]
			for doc in thisAtt:
				topicVals.append(doc[topic])
		else:
			topicVals.append(0.0)
		topicByAttribute[a].append(topicVals)
	for a in attribute: meanValues.append(numpy.mean(topicByAttribute[a]))
	return(meanValues)


dist = open('../Mallet/documentTopics30.txt').readlines()
paperDist, dayDist, weekDist = read_dist(dist)

attLabels = papers

meanValues = topic_per_attribute(17, papers, paperDist)

plt.bar(range(len(attLabels)), meanValues, align="center")
#plt.suptitle("Topic 0: Identity/Education")
plt.suptitle(" 'Brokenshire by Paper", fontsize=30)

ax = plt.subplot() 
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontname('Arial')
    label.set_fontsize(20)

plt.xticks(range(len(attLabels)), attLabels)


plt.show()