class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i , item in enumerate(nums):
            if nums[i] == nums[i -1] and i > 0:
                continue

            if i + 1 > len(nums):
                break
            
            left, right = i+1 , len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left +=1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left] , nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left+= 1
        return res

""" 
[-4, -1 , -1, 0, 1, 2]
 0.  1.   2.  3. 4. 5
i     = 2
left  = 3
right = 4
"""