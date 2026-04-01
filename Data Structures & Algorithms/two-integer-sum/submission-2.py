class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for index, num in enumerate(nums):
            complementary = target - num 
            if complementary in nums_map.keys():
                return [min(index, nums_map[complementary]), max(index, nums_map[complementary])]
            nums_map[num] = index
        
        return []