import heapq
import itertools
 
 
class PriorityQueue(object):
    """Copied from here: https://docs.python.org/3.6/library/heapq.html#priority-queue-implementation-notes"""
 
    def __init__(self, heap=[]):
 
        heapq.heapify(heap)
        self.heap = heap
        self.entry_finder = {}
        self.REMOVED = '<remove_marker>'
        self.counter = itertools.count()
 
    def insert(self, node, priority=0):
        "Add a new node or update the priority of an existing node"
 
        if node in self.entry_finder:
            self.delete(node)
        count = next(self.counter)
        entry = [priority, count, node]
        self.entry_finder[node] = entry
        heapq.heappush(self.heap, entry)
 
    def delete(self, node):
        "Mark an existing node as REMOVED.  Raise KeyError if not found."
 
        entry = self.entry_finder.pop(node)
        entry[-1] = self.REMOVED
 
    def pop(self):
        "Remove and return the lowest priority node. Raise KeyError if empty."
 
        while self.heap:
            priority, count, node = heapq.heappop(self.heap)
            if node is not self.REMOVED:
                del self.entry_finder[node]
                return priority, node
        raise KeyError('pop from an empty priority queue')
