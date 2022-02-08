class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Outer loop from 1st to 2nd last integer
        for i in range(len(nums) - 1):
            # Inner loop comparing i to all other integers (no repeat pairs)
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]