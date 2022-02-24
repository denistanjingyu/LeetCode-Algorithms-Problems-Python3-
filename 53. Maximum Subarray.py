class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Key idea: prior positive no. can increase the value of subsequent no. by summation
        # For example: given [2, 1], 2 can increase 1 value to 3 [2, 3]
        # 3 is now a sum of the prior value and its own original value
        # Each index can be the sum of all previous values (if positive contribution)
        # Only need to compare current index to previous index as the previous index takes care
        # of the overall contribution of its own previous index
        # e.g. index 2 takes care of index 1; index 3 takes cares of index 2 which include 1
        # If no positive numbers, return the largest among negative numbers
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        
        return max(nums)