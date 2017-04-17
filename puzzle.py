
"""
Given letters EGIVRVONL, find out all possible words having following condtion:
    -- Each letter must be appear exacly once
    -- Letter r must be there
    -- Word lenght must be atleast 6

"""
import nltk

def find_words(letters):
    puzzle_letters = nltk.FreqDist(letters)
    word_list = nltk.corpus.words.words()
    _obligatory = 'r'

    for w in word_list:
        if len(w) >=6 and _obligatory in w and nltk.FreqDist(w) <= puzzle_letters:
            print w


if __name__ == '__main__':
    find_words('egivrvonl')
