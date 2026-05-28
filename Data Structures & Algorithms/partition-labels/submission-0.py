class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        size = end = 0

        lastIndex = {} # char -> last index

        for i , v in enumerate(s):
            lastIndex[v] = i

        for i , v in enumerate(s):
            size += 1
            end = max(end, lastIndex[v])

            if i == end:
                res.append(size)
                size = 0
        
        return res