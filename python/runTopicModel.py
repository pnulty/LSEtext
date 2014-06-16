import codecs
from os import listdir
from os.path import isfile, join
from gensim import corpora, models, similarities
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
stopfile = "/home/paul/Dropbox/LSETextMining/code/stopwords.txt"
stopwords = [s.strip() for s in codecs.open(stopfile,encoding='utf-8').readlines()]
for m in news_corpus.documents:
	words = m.text.split()
	words = filter(lambda word: word not in stopwords, words)
	texts.append(words)

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/irl.mm', corpus)
corpus_bow = corpora.MmCorpus('/tmp/irl.mm')

tfidf = models.TfidfModel(corpus_bow)
corpus_tfidf = tfidf[corpus_bow]
#print corpus_tfidf
#print dictionary
ldamodel = models.LdaModel(corpus_bow, id2word=dictionary, num_topics=20)

#ldamodel = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=20)


for j in ldamodel.show_topics(topn=40):
	print j
	print "\n ** next ** \n"

