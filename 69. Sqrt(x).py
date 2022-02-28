class Solution:
    def mySqrt(self, x: int) -> int:
        # Point left and right to 0 and the given number (account for 0 and 1)
        l, r = 0, x
        
        # Binary search through the range of values from 0 to x
        # Want to return mid when x is between mid^2 and (mid+1)^2
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
    
        return mid