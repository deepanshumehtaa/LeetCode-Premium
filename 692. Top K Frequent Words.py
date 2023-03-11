"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

["i", "love", "leetcode", "i", "love", "coding", "and", "love", "you", ]

o/p: ['love', 'i', 'leetcode']
"""

from collections import Counter
from heapq import nsmallest


def topKFrequent(words: List[str], k: int) -> List[str]:
    """
    Max Heap
    Time Complexity: O(N + k\log{N})O(N+klogN)
    """
    cnt = Counter(words)
    return heapq.nsmallest(n=k, iterable=cnt.keys(), key=lambda x: (-cnt[x], x))


def topKFrequent1(words: List[str], k: int) -> List[str]:
    """
    the classic way with MAX heap
    """
    cnt = Counter(words)
    
    h = []
    for key, freq in cnt.items():
        heapq.heappush(h, (-freq, key))
        if len(h) > k:
            h.pop(-1)  # equivalent to `pop()`

    h.sort(key=lambda x: -x[0], reverse=True)
    return [i for _, i in h]

    
    
"""Min Heap"""

from collections import Counter
from heapq import heappush, heappop


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        h = []
        for word, freq in cnt.items():
            heappush(h, Pair(word, freq))
            if len(h) > k:
                heappop(h)
        return [p.word for p in sorted(h, reverse=True)]

    
