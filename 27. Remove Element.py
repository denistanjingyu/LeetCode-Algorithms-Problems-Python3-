class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Add a header k to track number of elements at the end and assign valid no.
        k = 0
        
        # Loop through entire array
        # Assign valid integer at k and increase k by 1
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
        
        return k