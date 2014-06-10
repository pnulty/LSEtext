import codecs
from os import listdir
from os.path import isfile, join
import gensim
import string
import nltk
import quanteda
import sys
import random



def make_docs(docs):
	new_docs=[]
	for d in docs:
		lines = d[0]
		filename = d[1]
		atts = lines[0]
		text = '\n'.join(lines[1:])
		new_docs.append(quanteda.Document(text, filename, atts))
	return new_docs


def read_docs(di):
	docs=[]
	file_list = [join(di,f) for f in listdir(di) if isfile(join(di,f)) ]
	for f in file_list:
		docs.append([codecs.open(f,encoding='utf-8').readlines(),f])
	return docs


inpath = "/home/paul/Dropbox/LSETextMining/code/articles"
docs = read_docs(inpath)
news_corpus = quanteda.Corpus()
temp = make_docs(docs)
news_corpus.documents.extend(temp)
news_corpus.preprocess()


texts=[]
for m in news_corpus.documents:
	words = m.text.split()
	texts.append(words)

dictionary = gensim.corpora.Dictionary(texts)
dictionary = gensim.corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
gensim.corpora.MmCorpus.serialize('/tmp/irl.mm', corpus)
corpus = gensim.corpora.MmCorpus('/tmp/irl.mm')

tfidf = gensim.models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
print corpus_tfidf
print dictionary
lsi = gensim.models.lsimodel.LsiModel(corpus=corpus, id2word=dictionary, num_topics=400)
lsi.print_topics(10)

#model = gensim.models.ldamodel.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=10, update_every=0, passes=10)
#model.show_topics(10)
#for j in model.print_topics(10):
#	print j
#	print "\n ** next ** \n"
