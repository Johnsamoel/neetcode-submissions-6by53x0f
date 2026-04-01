class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums) 
        longest = 0
    
        for item in nums:
            if (item - 1) not in numsSet:
                curr_len = 0
                while (item + curr_len) in numsSet:
                    curr_len += 1
                longest = max(longest , curr_len)

        return longest           