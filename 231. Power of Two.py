class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Power of two if can be continuously divided by 2 till 1
        if n == 1:
            return True

        while n > 1:
            n /= 2
            
        return n == 1