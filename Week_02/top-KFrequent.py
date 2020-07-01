from collections import defaultdict
import heapq

class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, another):
        if self.freq == another.freq:
            return self.word > another.word
        else:
            return self.freq < another.freq

    def __eq__(self, another):
        return self.freq == another.freq and self.word == another.word

class Solution:
    def topKFrequent(self, words, k):
        d = defaultdict(int)
        for w in words:
            d[w] += 1
        heap = []
        for k, v in d.items():
            if len(heap) == k:
                heapq.heapreplace(heap, Word(k, v))
        res = []

