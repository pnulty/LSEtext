"""Read documents downloaded from factiva and split into articles
with relevant attributes
"""

from os import listdir
from os.path import isfile, join

def read_docs(di):
	docs=[]
	file_list = [join(di,f) for f in listdir(di) if isfile(join(di,f)) ]
	for f in file_list:
		docs.append(open(f).read())
	return docs

def split_docs(doc):
	#print doc
	articles = doc.split("____________\n")
	paper_codes = []
	return articles

def parse_article(art):
	lines = art.split("\n")
	print lines

d = "C:\\Users\\Paul\\Dropbox\\LSETextMining\\code\\articles"
docs = read_docs(d)
articles = [] 
for d in docs: articles.extend(split_docs(d))
for a in articles[4:15]: parse_article(a)