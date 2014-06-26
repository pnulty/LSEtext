import collections
import matplotlib.pyplot as plt
import numpy
import sys
import time
""" Read in the Mallet output file and analyse the topic distribution"""



"""initialize mappings of papers, days and weeks to posterior
document topic distributions"""
def read_dist(dist):
	dayDist = collections.defaultdict(list)
	print len(dist)
	for d in dist:
		day=d.split()[1]
		day = time.strptime(day, "%Y-%m-%d").tm_yday
		dayDist[day].append([float(n) for n in d.split()[2:]])
	return(dayDist)



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


dist = open('../Mallet/documentTopics40TweetsByTweetFilt.txt').readlines()
dayDist = read_dist(dist)

attLabels = dayDist.keys()
print attLabels


meanValues = topic_per_attribute(31, attLabels, dayDist)

plt.bar(range(len(attLabels)), meanValues, align="center")
#plt.suptitle("Topic 0: Identity/Education")
plt.suptitle("UKIP/Vote/EU topic from all tweets by Day", fontsize=30)

ax = plt.subplot() 
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontname('Arial')
    label.set_fontsize(20)

plt.xticks(range(len(attLabels)), attLabels)


plt.show()