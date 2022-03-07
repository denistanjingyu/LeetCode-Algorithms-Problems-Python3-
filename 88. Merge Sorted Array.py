class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Stay in the loop as long as there's 1 element from each array to compare
        # Since both arrays are sorted, the pairwise comparison will be based on the m&n pointers
        # Alter nums1 inplace from the back (replace 0s instead of valid elements at the front)
        # Iteratively replace the current element with the larger value from num1/num2
        # Since nums1 has to accommodate for nums2 elements, m will reach 0 before n
        # Final if statement to append the remaining smaller elems from num2 to front of nums1
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        if n > 0:
            nums1[0:n] = nums2[0:n]