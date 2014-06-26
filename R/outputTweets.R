library(quanteda)

load('/home/paul/Dropbox/LSETextMining/data/tweets/15thMay.RData')
allResults1 <- allResults
allResults <- data.frame()
load('/home/paul/Dropbox/LSETextMining/data/tweets/16thMay.RData')
allResults2 <- allResults
allResults <- data.frame()
load('/home/paul/Dropbox/LSETextMining/data/tweets/17thMay.RData')
allResults3 <- allResults
allResults <- data.frame()

load('/home/paul/Dropbox/LSETextMining/data/tweets/18thMay.RData')
allResults4 <- allResults
allResults <- data.frame()
load('/home/paul/Dropbox/LSETextMining/data/tweets/19thMay.RData')
allResults5 <- allResults
allResults <- data.frame()
load('/home/paul/Dropbox/LSETextMining/data/tweets/20thMay.RData')
allResults6 <- allResults
allResults <- data.frame()

load('/home/paul/Dropbox/LSETextMining/data/tweets/21stMay.RData')
allResults7 <- allResults
allResults <- data.frame()
load('/home/paul/Dropbox/LSETextMining/data/tweets/22ndMay.RData')
allResults8 <- allResults
allResults <- data.frame()


allResults <- rbind(allResults1,allResults2,allResults3,allResults4,allResults5,allResults6,allResults7,allResults8 )
#430,000 tweets
#174686 non-retweets

origTweets <-subset(allResults, isRetweet==FALSE)
origTweets$text <- gsub(',','', origTweets$text)
origTweets$text <- gsub('\n','', origTweets$text)
origTweets$text <- gsub('\r','', origTweets$text)
byUser <- origTweets[,c("text","screenName", 'created')]
atts <- origTweets[,c("screenName", "created")]
#x <- corpusCreate(clean(byUser$text), attribs = atts, textnames=row.names(byUser))
