class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        postfix= 1
        res= [1] * n

        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]
  
        for i in range(n - 2, -1, -1):
            postfix *= nums[i + 1]
            res[i]  *= postfix

        return res