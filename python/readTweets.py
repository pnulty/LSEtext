import codecs
import collections

junkScore = 0.0
ukScore = 0.0
notUKScore = 0.0

junkWords = []

notUKWords = ['obama']


def filter_uk_tweets(allTweets):
	ukTweets = []
	junkWords =['']
	ukWords = ['farage','miliband', 'cameron','eu', 'british', 'ukip']
	

	for t in allTweets:
		uks =0.0
		words = t.split()
		newwords = []
		for w in words:
			if w in ukWords:
				uks+=1.0
			else:
				newwords.append(w)
		if uks > 0.0 : ukTweets.append(' '.join(newwords) )
		print (uks/float(len(words)))
	return(ukTweets)

lines = codecs.open('../tweets/allTweets.csv',encoding='utf-8-sig', errors='ignore').readlines()
out = open('../tweets/malletFormByTweetFiltered.txt', 'w+')
tweets = []
dates = []
users = collections.defaultdict(set)

for line in lines:
	if 'http' in line: continue
	#print line.encode('ascii', 'ignore')
	line = line.split(',')
	user = line[2].strip()
	text = line[1].strip()
	if len(text) < 25: continue
	text = text.lower()
	date = line[3].strip()
	if len(date.split()) >1: date = date.split()[0]
	text = ''.join([c for c in text if (c.isalnum() or c==' ')])
	tweets.append(text)
	dates.append(date)
	users[user].add(text)





tweets = filter_uk_tweets(tweets)

i=0
while i < len(tweets):
	out.write(str(i)+ " " + tweets[i].encode('ascii', 'ignore'))
	out.write('\n')
	i+=1
print i

# i=0
# for u in users:
# 	i=i+1
# 	text = '. '. join(users[u])
# 	out.write(str(i) + " " + text.encode('ascii', 'ignore'))
# 	out.write('\n')
# print i