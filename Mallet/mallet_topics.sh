/home/paul/Mallet/bin/mallet import-dir --input ../mergedArticlesTime --output topic-files.mallet \
  --keep-sequence --remove-stopwords --extra-stopwords ../stopwords.txt


/home/paul/Mallet/bin/mallet train-topics --input topic-files.mallet \
  --num-topics 30  --optimize-interval 20 --output-state topic-state.gz --output-doc-topics documentTopics30FT.txt --output-topic-keys 30keysFT.txt


