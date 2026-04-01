class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        res = []

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                res.append(left + 1)
                res.append(right + 1)
                return res
        return res





""" 
rules:
1. you cannot use the same element twice
2. arr is sorted 
3. return 1-indexed list which means i + 1 
4. smaller index should be first in the result
"""
        