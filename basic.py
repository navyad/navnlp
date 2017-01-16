def find_lexical_richness(sample_text):
    """
    on average how many tiimes a each word text appeared
    """
    print len(sample_text) / len(set(sample_text))


def word_count(sample_text, word):
    """
    how often a word appeared in a text
    """
    return sample_text.count(word)


def word_count_percentage(sample_text, word):
    """
    how often a word appeared in a text
    """
    _count = word_count(sample_text, word)
    return 100 * _count / len(sample_text)
