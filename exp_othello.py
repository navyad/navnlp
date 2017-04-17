from nltk.corpus import stopwords, shakespeare
import nltk


file_name = 'othello.xml'
_all_words = shakespeare.words(file_name)

# exclude stopwords
print "Total words \n"
_words = [x for x in _all_words if x not in stopwords.words() and x.isalpha()]
print "total words", len(_words)


# 10 most frequent words
print "Most 10 frequent words \n"
text_obj = nltk.Text(_words)
freq = nltk.FreqDist(text_obj)
top_ten_words = freq.most_common()[:10]    # list of tuple
for tp in top_ten_words:
    print tp[0], tp[1]

# number of words which occured only once
print "Number of words appeared only once {0}".format(len(freq.hapaxes()))
