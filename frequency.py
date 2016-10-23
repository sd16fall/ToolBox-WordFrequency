""" Analyzes the word frequencies in a book downloaded from
        Project Gutenberg
     Some oddness caused by unicode charachters that python cannot interperet"""

import string

def get_word_list(file_name):
        """ Reads the specified project Gutenberg book.  Header comments,
                punctuation, and whitespace are stripped away.  The function
                returns a list of the words used in the book as a list.
                All words are converted to lower case.
                
        """
        
        f = open(file_name ,'r')
        lines = f.readlines()
        curr_line = 0
        #strips away header file
        while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
                curr_line += 1
        lines = lines[curr_line+1:]
        #takes list of words line by line, recombines to mass of text
        rawtext = ""
        for i in lines:
                rawtext += i
        #strips out punctuation
        for i in string.punctuation:
                rawtext = rawtext.replace(i,' ')
        #close file and return list of words
        rawtext.lower()
        f.close()
        return rawtext.split()
        
        
        
def get_top_n_words(word_list, n):
        """ Takes a list of words as input and returns a list of the n most frequently
                occurring words ordered from most to least frequently occurring.

                word_list: a list of words (assumed to all be in lower case with no
                                        punctuation
                n: the number of words to return
                returns: a list of n most frequently occurring words ordered from most
                                 frequently to least frequentlyoccurring
        """

        word_counter = {}
        #loops thru list, adds one if word is in dictionary, if not makes entry with value 1
        for word in word_list:
                if word in word_counter:
                        word_counter[word] += 1
                else:
                        word_counter[word] = 1
        #sory word_counter by word frequency
        top_words = sorted(word_counter, key = word_counter.get, reverse = True)

        return top_words[:n]

print get_top_n_words(get_word_list('Tom_Sawyer.txt'),100)
