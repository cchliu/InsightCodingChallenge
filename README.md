# InsightCodingChallenge
Insight Data Engineering - Coding Challenge
===========================================================
## Challenge Summary

This challenge is to implement two features:

1. Calculate the total number of times each word has been tweeted.
2. Calculate the median number of *unique* words per tweet, and update this median as tweets come in.

## Implementation Ideas

Main Program:

1) Feature #1: Calculate the total number of times each word has been tweeted.

- Use _Python_ Counter to create a hashtable for words, where the key is the word itself, and value is the
frequency of this word appeared so far.
    
2) Feature #2: Calculate the median number of *unique* words per tweet, and update this median as tweets come in.

- a) The most basic way is to store all the number of *unique* words of each tweet in a list, and calculate the median of this list each time a new tweet comes in (and there is a built-in function in numpy). Finding median in an unsorted array can be done in a linear time *O(n)*. If there are in total *n* tweets in the input file, the time complexity of realizing feature #2 will be *O(n^2)*. The space complexity is *O(n)*.
    
- b) However, method a) will redo the "find-median" process every time there is a new number added to the list, which won't take advantage the result of last run. This problem actually falls into the category of "streaming median" or "running median". One solution is called "max heap/min heap solution". Its time complexity is *O(nlogn)*, while space complexity is *O(n)*.

	- Tweets_v2.py uses this algorithm to realize feature #2. 
    
- c) While method b) is efficient, it is a more general solution because it applies for most of the data types. With that said, there may exist a specialized solution for this paritcular problem which is more efficient both in time and space, if taking into account the characteristics of tweets. And the answer is YES. Since Twitter limits tweet length to 140 characters, we may well use counting sort algorithm, whose time complexity is *O(kn)*, *k* is a constant and space complexity is *O(k)*. 

	- Tweets_v1.py uses this algorithm to realize feature #2. 

## Language and Modules
The program is implemented in _Python_. Python version is Python 2.7.6. No additional modules needed.

## Source File Description
	├── src 
	    ├── Tweets_v1.py 
        ├── Tweets_v2.py 
        ├── Heap.py
        ├── cal_streaming_median.py
        ├── file_IO.py
    a) Heap class is defined in Heap.py
    b) I/O functions are defined in file_IO.py
    c) Two solutions for calculating streaming median is defined in cal_streaming_median.py.
    d) Tweets_v1.py and Tweets_v2.py are the same in implementing feature #1, but differ at feature #2.
       Tweets_v1.py uses "counting sort" algorithm to calculate streaming median.
       Tweets_v2.py uses "max heap/min heap" algorithm to calculate streaming median.
