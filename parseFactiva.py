"""Read documents downloaded from factiva and split into articles
with relevant attributes
"""
import codecs
from os import listdir
from os.path import isfile, join

def read_docs(di):
	docs=[]
	file_list = [join(di,f) for f in listdir(di) if isfile(join(di,f)) ]
	for f in file_list:
		docs.append(codecs.open(f,encoding='utf-8').read())
	return docs

def split_docs(doc):
	#print doc
	articles = doc.split("____________")
	print len(articles)
	return articles



def paper_mapping():
	mapping = codecs.open('paperMappings.txt',encoding='utf-8').readlines()
	papermap = []
	for line in mapping:
		parts = line.split(':')
		oldnames = parts[0].split(',')
		newname = parts[1].strip()
		papermap.append((oldnames,newname))
	print papermap
	return papermap

def parse_article(art, ident, paper_names, papermap):
	outpath = "/home/paul/Dropbox/LSETextMining/code/mergedArticles"
	this_paper = 'error'

	lines = art.split("\n")
	lines = [line.replace('\r','') for line in lines if len(line)>1]
	for line in lines[0:10]:
		if line in paper_names:
			mapped = False
			for p in papermap:
				if line in p[0]:
					print line
					this_paper = str(p[1])
					mapped = True
			if not mapped: this_paper = line
	fname = this_paper+'_'+ident+'.txt'
	jsn = '{"newspaper":'+'"'+this_paper+'",'+'"id:"'+ident+'"}'

	outfile = codecs.open(join(outpath,fname), "w", "utf-8")
	outfile.write(jsn+"\n")
	for line in lines:
		outfile.write(line+"\n")
	outfile.close()


d = "/home/paul/Dropbox/LSETextMining/code/documents"

docs = read_docs(d)
articles = [] 
paper_names=codecs.open('newspaperNames.txt',encoding='utf-8').readlines()
papermap = paper_mapping()
paper_names = [p.strip() for p in paper_names]
for d in docs: articles.extend(split_docs(d))

print len(articles)
i = 0
for a in articles:
	parse_article(a,str(i),paper_names,papermap)
	i+=1
