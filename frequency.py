""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    fp = open(file_name,'r')
    lines = fp.readlines()
    curr_line = 0

    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]

    def process_line(line, word_list):
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            word_list.append(word)

    word_list = []
    for line in lines:
        process_line(line, word_list)

    return word_list

def get_top_n_words(word_list, n=100):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    hist = dict()
    for i in range(len(word_list)):
        word = word_list[i]
        hist[word] = hist.get(word, 0) + 1

    def most_common(hist):
        t = []
        for key, value in hist.items():
            t.append((value, key))
        t.sort(reverse=True)
        return t

    t = most_common(hist)
    print 'The most common words are:'
    for freq, word in t[0:n]:
        print word, '\t', freq


words = get_word_list('pg32325.txt')
get_top_n_words(words, 10)
