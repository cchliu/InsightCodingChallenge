#########################################
## THIS FILE CONTAINS I/O FUNCTIONS    ##
#########################################
import csv

def write_median(outfile, result, num_tweets):
    if num_tweets == 1: # first tweet
        mode = 'wb' # create a new output file
    else: 
        mode = 'ab' # append to output file
    with open(outfile, mode) as ff:
        writer = csv.writer(ff, delimiter='\t', quoting=csv.QUOTE_NONE)
        # The FAQ asks for one decimal precision
        writer.writerow(["{0:.1f}".format(result)])
        

#file.write("{:<27} {}\n".format(*item))
def write_wordcount(outfile, words_dict):
    with open(outfile, 'wb') as ff:
        writer = csv.writer(ff, delimiter='\t', quoting=csv.QUOTE_NONE)
        for key in sorted(words_dict.keys()):
            writer.writerow(["{0:<50} {1}".format(key, words_dict[key])])
                 
