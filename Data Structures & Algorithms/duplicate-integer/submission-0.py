class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numsSet = set()

        for num in nums:
            if num in numsSet:
                return True
            else:
                numsSet.add(num)
        return False
        