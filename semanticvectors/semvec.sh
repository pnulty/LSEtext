rm -r /home/paul/semvec/positional_index
java pitt.search.lucene.IndexFilePositions -minfrequency 3 -porterstemmer independent/
java pitt.search.semanticvectors.BuildPositionalIndex -stoplistfile /home/paul/semvec/stopwords.txt -luceneindexpath /home/paul/semvec/positional_index -windowradius 25 
#java pitt.search.semanticvectors.Search -queryvectorfile termtermvectors.bin -numsearchresults 50  immigr

java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr foreign
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr work
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr jobseek
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr claim
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr romanian
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr bulgarian
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr work
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr illeg
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr invad
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr invas
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr threat
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr school
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr veil
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr islam
java pitt.search.semanticvectors.CompareTerms -queryvectorfile termtermvectors.bin immigr terror


