#/home/paul/Mallet/bin/mallet import-dir --input ../mergedArticles --output topic-files.mallet \
#  --keep-sequence --remove-stopwords --extra-stopwords ../stopwords.txt

/home/paul/Mallet/bin/mallet train-topics --input topic-files.mallet \
  --num-topics 20  --optimize-interval 20 --output-state topic-state.gz --output-doc-topics documentTopics.txt

