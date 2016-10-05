""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

#	"""Reads the specified project Gutenberg book.  Header comments,
#		punctuation, and whitespace are stripped away.  The function
#		returns a list of the words used in the book as a list.
#		All words are converted to lower case.
#	"""

import string

def get_word_list(file_name):
    #opens file and stores a list of lines
    f = open(file_name ,'rU')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]

    #list of punctuation
    punct = string.punctuation #all punctuation
    punct_list = list(punct) #punctuation in a list -> len(punct_list) = 32
    punct_list.append(list(string.whitespace))

    #strip whitespace and punctuation
    new_lines = []
    for line in lines:
        for char in line:
            if char in punct_list:
                char = ''
            line = line.lower()
        new_lines.extend(line.split())

    return new_lines

# 	""" Takes a list of words as input and returns a list of the n most frequently
# 		occurring words ordered from most to least frequently occurring.
# 		word_list: a list of words (assumed to all be in lower case with no
# 					punctuation
# 		n: the number of words to return
# 		returns: a list of n most frequently occurring words ordered from most
# 				 frequently to least frequentlyoccurring
# 	"""

def get_top_n_words(word_list, n):
    word_counts = {}
    for word in word_list:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] +=1

    #print word_counts

    for key in sorted(word_counts, key = word_counts.get, reverse = True)[:n]:
        print key, word_counts[key]

wlist = get_word_list('American Fairytales.txt')
get_top_n_words(wlist, 100)
