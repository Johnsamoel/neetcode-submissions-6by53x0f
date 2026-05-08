class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def backtrack(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if self.isPali(s, j, i):
                part.append(s[j : i + 1])
                backtrack(i + 1, i + 1)
                part.pop()

            backtrack(j, i + 1)

        backtrack(0, 0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True