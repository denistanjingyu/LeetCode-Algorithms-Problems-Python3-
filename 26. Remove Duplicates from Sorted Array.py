class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # The first number will always be unique
        # Define a variable to start comparing from the 2nd index and store the number of unique element
        k = 1
        
        # Loop through length of nums - 1 as we start comparing from 2nd index
        # If next number is different from previous number, replace the next available index with the unique number and increase k by 1 for the next slot
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i]:
                nums[k] = nums[i + 1]
                k += 1
        
        return k