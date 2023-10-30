import nltk
from nltk.stem import PorterStemmer
w=PorterStemmer()
print(w.stem('eating'))
print(w.stem('coming'))
print(w.stem('running'))
print(w.stem('sleeping'))
