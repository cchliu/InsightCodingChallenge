######################################################
## THIS FILE CONTAINS FUNCTION THAT                 ##
## CALCULATES STREAMING MEDIAN                      ##
######################################################
# MAX/MIN HEAP ALGO
def MaxMin_Heap_ALGO(max_heap, min_heap, num):
    # step 1: add next item to one of the heaps
    pivot = max_heap[0]
    if num < pivot:
        max_heap.push(num)
    else:
        min_heap.push(num)
        
    # step 2: balance the heaps (after this step heaps will be
    # either balanced or differ at most 1 item)
    while len(max_heap) - len(min_heap) > 1:
        min_heap.push(max_heap.pop())
    
    while len(min_heap) - len(max_heap) > 1:
        max_heap.push(min_heap.pop())
        
    # step 3: calculate median    
    if len(max_heap) == len(min_heap):
        return (max_heap[0] + min_heap[0]) / 2.0
    elif len(max_heap) > len(min_heap):
        return max_heap[0]
    else:
        return min_heap[0]
        
########################################################
# COUNTING SORT ALGO
def Counting_Sort_ALGO(histogram, num, num_tweets):
    # update histogram
    histogram[num-1] += 1
    # find median from histogram
    # even number of items
    if num_tweets % 2 == 0:
        tmp = 0
        index_1 = 0
        while tmp < num_tweets/2:
            tmp += histogram[index_1]
            index_1 += 1
                    
        index_2 = index_1
        while tmp < num_tweets/2+1:
            tmp += histogram[index_2]
            index_2 += 1
        return (index_1 + index_2) / 2.0
    else: 
        # odd number of items
        tmp = 0
        index = 0
        while tmp < (num_tweets+1) / 2:
            tmp += histogram[index]
            index += 1
        return index
         
        
