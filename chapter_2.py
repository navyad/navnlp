from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.corpus import wordnet as wn


def all_stopwords():
    """
    these words are filtered wout before processing
    """
    return stopwords.words('english')


def all_words():
    return words.words()


class TestCorpus:

    def __init__(self, cop):
        self.cop = cop

    def corpus_files(self):
        """
        returns all fiels under a corpus
        """
        return self.cop.fileids()

    def corpus_words(self, file_name):
        """
        returns words count
        """
        return self.cop.words(file_name)

    def corpus_sents(self, file_name):
        """
        return all sentence
        """
        return self.cop.sents(file_name)

    def corpus_content(self, file_name):
        """
        return file's content
        """
        return self.cop.raw(file_name)



class TestWordNet:

    def __init__(self, search_word):
        self.search_word = search_word

    def get_synsets(self):
        return wn.synsets(self.search_word)

    def word_description(self, synset):
        return synset.definition()

    def all_lemmas(self, synset):
        return synset.lemmas()

    def lemma_names(self, synset):
        return synset.lemma_names()
