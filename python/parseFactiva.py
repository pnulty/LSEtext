"""
Read documents downloaded from factiva and split into articles
with relevant attributes: and combine sources
together.
"""
import codecs
import re
from os import listdir
from os.path import isfile, join
import time

def read_docs(di):
	docs=[]
	file_list = [join(di,f) for f in listdir(di) if isfile(join(di,f)) ]
	for f in file_list:
		docs.append(codecs.open(f,encoding='utf-8').read())
	return docs

def split_docs(doc):
	#print doc
	articles = doc.split("____________")
	return articles

def get_time(metad):
	months = ["february 2014","march 2014", "april 2014", "may 2014"]
	day = time.strptime("1 January 2014", "%d %B %Y").tm_yday
	for line in metad:
		for m in months:
			if m in line and len(line) < 20:
				print line
				r = time.strptime(line, "%d %B %Y")
				day =  r.tm_yday
	if day < 10: print metad
	return day
	

def paper_mapping():
	temp = codecs.open('../paperMappings.txt',encoding='utf-8').readlines()
	mapping = [p.lower() for p in temp]
	papermap = []
	for line in mapping:
		parts = line.split(':')
		oldnames = parts[0].split(',')
		newname = parts[1].strip()
		papermap.append((oldnames,newname))
	return papermap

def parse_article(art, ident, paper_names, papermap):
	outpath = "/home/paul/Dropbox/LSETextMining/code/mergedArticlesTime"
	this_paper = 'error'

	lines = art.split("\n")
	lines = [line.replace('\r','') for line in lines if len(line)>1]
	for line in lines[0:10]:
		if line in paper_names:
			mapped = False
			for p in papermap:
				if line in p[0]:
					this_paper = str(p[1])
					mapped = True
			if not mapped: this_paper = line
	date = str(get_time(lines[2:11]))
	this_paper = this_paper.replace(' ','-')
	fname = this_paper+'_'+date+ '_'+ident+'.txt'
	
	jsn = '{"newspaper":'+'"'+this_paper+'",'+'"id:"'+ident+'","'+date+'"}'

	outfile = codecs.open(join(outpath,fname), "w", "utf-8")
	outfile.write(jsn+"\n")
	for line in lines:
		outfile.write(line+"\n")
	outfile.close()


d = "/home/paul/Dropbox/LSETextMining/code/documents"

docs = read_docs(d)
articles = [] 
temp=codecs.open('../newspaperNames.txt',encoding='utf-8').readlines()
paper_names = [p.lower() for p in temp]
papermap = paper_mapping()
paper_names = [p.strip() for p in paper_names]
for d in docs: articles.extend(split_docs(d))

print len(articles)
i = 0
for a in articles:
	"""downcase and remove punctuation"""
	a = a.lower()
	a=re.sub("[\.\t\,\:;\(\)\.\?\"\'']", "", a, 0, 0)
	a.strip()
	parse_article(a,str(i),paper_names,papermap)
	i+=1
