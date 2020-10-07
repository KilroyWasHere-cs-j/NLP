from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
import nltk


w = Word("Test")
b = TextBlob("I havv goood speling!")
print(b)
print("-to-")
print(b.correct())




w = Word("went")
print(w.lemmatize('v'))


definitions = Word('Hello').definitions
print(definitions)


