library(quanteda)
library(topicmodels)
library(lda)
library(ca)
data(stopwords)
custom_stopwords <- readLines('/home/paul/Dropbox/LSETextMining/code/stopwords.txt')
  
  

path = '/home/paul/Dropbox/LSETextMining/code/articles'
attNames = c("paperName", "id")
newsCorpus <- corpusFromFilenames(path, attNames, sep = "_")
paperCount <- table(newsCorpus$attribs$paperName)
topPapers<- names(sort(paperCount, decreasing = TRUE)[1:21])
reducedCorpus <- subset(newsCorpus, paperName %in% topPapers)

reducedByPaperDfm <- dfm(reducedCorpus, group = "paperName")
reducedDfmStopwords <- stopwordsRemove(reducedByPaperDfm, custom_stopwords)


trimByPaper <- dfmTrim(reducedDfmStopwords, minCount=1, minDoc=2) 
trimByPaperTm<- dfm2tmformat(trimByPaper)