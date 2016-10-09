import string

def get_word_list(file_name):
    #removes header
    f = open(file_name,'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    list_of_words = []
    #removes punctuations and returns list of words
    for sentence in lines:
        sentence = sentence.lower()
        sentence = sentence.translate(string.maketrans("",""), string.punctuation) #removes punctuations
        list_of_words.extend(sentence.split())
    return list_of_words


def get_top_n_words(words_list, n): #n represents the number of words to return in order of most frequent
    word_counts = {} #dictionary to store words and their count
    for word in words_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True) 
    for top_word in ordered_by_frequency[:n]:
        print top_word, word_counts[top_word]

d = get_word_list('/home/sandy/Desktop/sherlock.txt')
get_top_n_words(d, 100)
