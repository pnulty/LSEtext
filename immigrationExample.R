library(quanteda)
library(topicmodels)
library(lda)
library(ca)
custom_stopwords <- readLines('/home/paul/Dropbox/LSETextMining/code/stopwords.txt')



path = '/home/paul/Dropbox/LSETextMining/code/sample/'
attNames = c("paperName", "id")

newsCorpus <- corpusFromFilenames(path, attNames, sep = "_")

# filter out smaller papers
paperCount <- table(newsCorpus$attribs$paperName)
topPapers<- names(sort(paperCount, decreasing = TRUE)[1:21])
reducedCorpus <- subset(newsCorpus, paperName %in% topPapers)

# make a dfm and triplet matrix dfm from without grouping (just by doc)
byDocDfm <- dfm(reducedCorpus)
byDocDfmTrim <- dfmTrim(byDocDfm, minCount=1, minDoc=2) 
finalDfmByDoc <- stopwordsRemove(byDocDfmTrim, custom_stopwords)
finalDfmByDoc <- finalDfmByDoc[which(rowSums(finalDfmByDoc) > 0),] 
finalTripletByDoc<- dfm2tmformat(finalDfmByDoc)


#LDA models
ldaByDocVEM20 <- LDA(finalTripletByDoc, method="VEM", control = list(alpha = 0.1), k = 20)
ldaByDocVEMNoAlpha20 <- LDA(finalTripletByDoc, method="VEM", k = 20)
ldaByDocGibbs20 <- LDA(finalTripletByDoc, method="Gibbs", control = list(alpha = 0.1), k = 20)
ldaByDocGibbsNoAlpha20 <- LDA(finalTripletByDoc, method="Gibbs", k = 20)

#CTM models
ctmByDocVEM15 <- LDA(finalTripletByDoc, method="VEM", control = list(alpha = 0.1), k = 15)
ctmByDocVEMNoAlpha15 <- LDA(finalTripletByDoc, method="VEM", k = 15)
ctmByDocGibbs15 <- LDA(finalTripletByDoc, method="Gibbs", control = list(alpha = 0.1), k = 15)
ctmByDocGibbsNoAlpha15 <- LDA(finalTripletByDoc, method="Gibbs", k = 15)

get_terms(ctmByDocGibbsNoAlpha15, k=20)
#culture  = 3
#economic = 7

model <- ctmByDocGibbsNoAlpha15
topics <- topics(model)
postTopics <- posterior(model)$topics
leftPapers <- c("Guardian", "Independent")
rightPapers <- c("Express", "Mail")

reducedCorpus <- corpusAddAttributes(reducedCorpus, postTopics,name="posteriors")










# model <- ca(t(finalDfm), nd = 1)
# model2 <- ca(t(finalDfm), nd = 2)
# dotchart(model$colcoord[order(model$colcoord[,1]),1], labels = model$colnames[order(model$colcoord[,1])])
# plot(model2,what=c("none","active"))
# ldaResult <- lda.collapsed.gibbs.sampler(documents=td$documents, 
#                                                      K=3,  
#                                                      vocab=td$vocab,
#                                                      num.iterations=50, alpha=0.1, eta=0.1) 

