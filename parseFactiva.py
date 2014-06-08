import quanteda

""" read in RTF files downloaded from factiva, parse them into documents, and
associate each document with variables like source and date"""

def read_news(dir):
	pass


#main
articles=quanteda.Corpus()
d = "newsArticles"
articles.read_docs(d)

print articles.documents[4].text