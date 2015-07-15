import heapq

class MinHeap(object):
    """ A neat min-heap wrapper """
    def __init__(self):
        self._heap = []
        
    def push(self, item):
        heapq.heappush(self._heap, item)
        
    def pop(self):
        return heapq.heappop(self._heap)
        
    def __len__(self):
        return len(self._heap)
        
    def __iter__(self):
        return iter(self._heap)
    
    def __getitem__(self, key):
        return self._heap[key]
        
        
class MaxHeap(object):
    """ A neat max-heap wrapper """
    def __init__(self):
        self._heap = []
        
    def push(self, item):
        heapq.heappush(self._heap, item*-1)
        
    def pop(self):
        return heapq.heappop(self._heap)*-1
        
    def __len__(self):
        return len(self._heap)
        
    def __iter__(self):
        return iter(self._heap)
        
    def __getitem__(self, key):
        return self._heap[key]*-1
