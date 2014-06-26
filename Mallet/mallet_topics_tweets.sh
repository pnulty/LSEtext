/home/paul/Mallet/bin/mallet import-file  --input /home/paul/Dropbox/LSETextMining/code/tweets/malletFormByTweetFiltered.txt \
  --keep-sequence --remove-stopwords --extra-stopwords ../stopwords.txt --output tweets.mallet


/home/paul/Mallet/bin/mallet train-topics --input tweets.mallet \
  --num-topics 35  --optimize-interval 20 --output-state topic-state.gz --output-doc-topics documentTopicsFiltered.txt --output-topic-keys keysFiltered.txt


