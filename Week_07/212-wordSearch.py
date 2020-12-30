from collections import defaultdict

ENDOFW = "#"
dx = [-1,1,0,0]
dy = [0,0,-1,1]

class Solution:
    def dfs(self, cur_word, i, j, board, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if ENDOFW in cur_dict:
            self.res.add(cur_word)
        tmp, board[i][j] = board[i][j], "@"
        for k in range(4):
            x, y = i+dx[k], j+dy[k]
            if x in range(self.m) and y in range(self.n) and board[x][y] in cur_dict:
                self.dfs(cur_word, x, y, board, cur_dict)
        board[i][j] = tmp
        
    def findWords(self, board, words):
        if not board or not board[0] or not words:
            return []
        self.res = set()
        self.m = len(board)
        self.n = len(board[0])
        
        #build a trie first
        root = defaultdict()
        for word in words:
            node = root
            for w in word:
                node = node.setdefault(w, {})
            node[ENDOFW] = ENDOFW
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self.dfs('', i, j, board, root)
        return self.res
        
