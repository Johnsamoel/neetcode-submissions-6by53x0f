class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # to avoid duplicates

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            
            # Step 1: pick the item
            # 1.1 do 
            subset.append(nums[i])
            # 1.2 recurse
            backtrack(i + 1, subset)
            # 1.3
            subset.pop()

            # skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            # step 2: skip the item
            backtrack(i + 1, subset)

        backtrack(0, [])

        return res