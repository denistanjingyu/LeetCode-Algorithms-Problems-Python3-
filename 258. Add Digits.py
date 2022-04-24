class Solution:
    def addDigits(self, num: int) -> int:
        len_digits = None
        
        while len_digits != 1:
            sum_digits = sum([int(i) for i in str(num)])
            len_digits = len(str(sum_digits))
            
            if len_digits == 1:
                return sum_digits
            
            num = sum_digits