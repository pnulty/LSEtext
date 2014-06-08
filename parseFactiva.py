from os import listdir
from os.path import isfile, join

def read_news(dir):
	file_list = [ f for f in listdir(dir) if isfile(join(dir,f)) ]
	for f in file_list:

		doc = open(f).read()


def parse_articles(doc):
	articles = doc.split("____________\n")
	print len(articles)
	paper_codes = []
	return

d = "C:\\Users\\Paul\\lsetemp\\LSEtext\\articles"

fs = read_news(d)

articles = []
for f in fs:
	articles.append(parse_articles(f))