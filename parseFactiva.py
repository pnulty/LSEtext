from os import listdir
from os.path import isfile, join

def read_news(di):
	docs=[]
	file_list = [join(di,f) for f in listdir(di) if isfile(join(di,f)) ]
	for f in file_list:
		docs.append(open(f).read())
	return docs




def parse_articles(doc):
	#print doc
	articles = doc.split("____________\n")
	print len(articles)
	paper_codes = []
	return articles

d = "C:\\Users\\Paul\\Dropbox\\LSETextMining\\code\\articles"
docs = read_news(d)
articles = []
for d in docs:
	articles.extend(parse_articles(d))
print(len(articles))