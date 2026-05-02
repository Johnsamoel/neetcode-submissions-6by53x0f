class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, subset, sum):
            # valid case
            if sum == target:
                res.append(subset.copy())
                return

            # invalid case
            if i >= len(nums) or sum > target:
                return

            # do
            subset.append(nums[i])

            # recurse
            # we need to use element more than once - mentioned in desc..
            backtrack(i, subset, sum + nums[i])

            # undo
            subset.pop()

            # recurse
            backtrack(i + 1, subset, sum)

        backtrack(0, [], 0)
        return res
