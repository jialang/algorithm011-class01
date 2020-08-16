class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank or not bank:
            return -1
        cs = ['A', 'C', 'G', 'T']
        dq = deque()
        dq.append((start,1))
        while dq:
            tmp, level = dq.popleft()
            for i in range(len(tmp)):
                oldC = tmp[i]
                for j in range(4):
                    tmp = tmp[:i] + cs[j] + tmp[i+1:]
                    if tmp == end:
                        return level
                    elif tmp in bank:
                        bank.remove(tmp)
                        dq.append((tmp, level+1))
                tmp = tmp[:i] + oldC + tmp[i+1:]
        return -1
