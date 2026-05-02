class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(0, [], nums)

        return self.res

    def backtrack(self, i, subset, nums):

        if i == len(nums):
            self.res.append(subset.copy())
            return

        # do
        subset.append(nums[i])

        # recurse
        self.backtrack(i + 1, subset, nums)

        # undo
        subset.pop()

        # recurse
        self.backtrack(i + 1, subset, nums)
