# IMPORT STANDARD PYTHON MODULES
import os
import csv
import numpy as np
import collections
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# IMPORT USER-DEFINED MODULES
from Heap import MinHeap
from Heap import MaxHeap
from cal_streaming_median import MaxMin_Heap_ALGO

from file_IO import write_median
from file_IO import write_wordcount
####################################################
# FILE I/O  #
####################################################
# SET INPUT FILE PATH
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
#input_file = root_dir + '/tweet_input/tweets.txt'
input_file = root_dir + sys.argv[1]

# WRITE WORDS FREQUENCY COUNT TO "ft1.txt"
# SET OUTPUT FILE PATH
#output_file_1 = root_dir + '/tweet_output/ft1_v2.txt' 
output_file_1 = root_dir + sys.argv[2]

# WRITE STREAMING MEDIAN TO "ft2.txt"
# SET OUTPUT FILE PATH
#output_file_2 = root_dir + '/tweet_output/ft2_v2.txt'  
output_file_2 = root_dir + sys.argv[3]
#####################################################
# MAIN PROGRAM #
#####################################################
# hashtable for counting words frequency
words_dict = collections.Counter()
# number of tweets processed
num_tweets = 0 

# max/min heap for calculating streaming median
max_heap = MaxHeap()
min_heap = MinHeap()

with open(input_file, 'rb') as ff:
    # let's read in one tweet at a time
    for line in ff:
        # parse this tweet into separate words
        tmp_words = line.rstrip('\n').split(' ')
        
        # calculate total number of times each word tweeted
        for word in tmp_words:
            if word != '':
                words_dict[word] += 1
                            
        # we have processed one tweet
        num_tweets += 1
                  
        # calculate the median number of unique words per tweet
        num_uwords = len(set(tmp_words)) # number of unique words in this tweet
        if num_tweets == 1:
            max_heap.push(num_uwords)
            median = max_heap[0]
        else:
            median = MaxMin_Heap_ALGO(max_heap, min_heap, num_uwords)
        write_median(output_file_2, median, num_tweets) 

# WRITE WORDS FREQUENCY COUNT TO "ft1.txt"
write_wordcount(output_file_1, words_dict)
                 
