class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        
        while n > 1:
            return self.isPowerOfThree(n/3)