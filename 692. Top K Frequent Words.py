"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

["i","love","leetcode","i","love","coding"]
2
"""

from collections import Counter
from heapq import nsmallest


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Max Heap
        Time Complexity: O(N + k\log{N})O(N+klogN)
        """
        cnt = Counter(words)
        return nsmallest(k, cnt.keys(), key=lambda x: (-cnt[x], x))
    
    
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

    
