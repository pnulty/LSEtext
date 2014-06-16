"""convert files from rtf to plaintext"""
import os
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter

outpath = "plaintextDocs"
inpath =  "newsArticles"
fnames = os.listdir(inpath)

for f in fnames:
	try:
		doc = Rtf15Reader.read(open(inpath+'/'+f, "rb"))
	except:
		print f
		continue
	of = open(outpath+'/'+f, 'w+')
	of.write(PlaintextWriter.write(doc).getvalue())
#	for x in doc.content:
#		of.write(x.content)
