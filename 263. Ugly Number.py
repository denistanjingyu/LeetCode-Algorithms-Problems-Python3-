class Solution:
    def isUgly(self, n: int) -> bool:
        prime_list = [2, 3, 5]
        
        for prime_num in prime_list:
            while n % prime_num == 0 < n:
                n /= prime_num
            
        return n == 1