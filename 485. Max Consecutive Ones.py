class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr = 0

        for digit in nums:
            if digit == 0:
                curr = 0

            elif digit == 1:
                curr += 1
                if curr > max_ones:
                    max_ones = curr
        return max_ones