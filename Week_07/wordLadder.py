from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.length = 0
        self.all_combo_dict = defaultdict(list)


    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            tmp = current_word[:i] + "*" + current_word[i+1:]
            for word in self.all_combo_dict[tmp]:
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None


    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        self.length = len(beginWord)
        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Queues for birdirectional BFS
        queue_begin = deque([(beginWord, 1)]) # BFS starting from beginWord
        queue_end = deque([(endWord, 1)]) # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0

s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(s.ladderLength(beginWord, endWord, wordList))
