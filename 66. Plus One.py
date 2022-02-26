class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Define a variable to point to last digit
        i = len(digits) - 1
        
        # Case 1: last digit is not 9, simply add 1 to it and return answer (98 -> 99)
        if digits[i] != 9:
            digits[i] += 1
            return digits
        
        # Case 2: last digit is 9 and prev digit can be 9 also and so on
        # While loop to switch all 9s to 0
        # If all digits are 9s, insert a 1 at 0 index and return answer (99 -> 100)
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
            if i < 0:
                digits.insert(0, 1)
                return digits
        
        # If not all digits are 9s, simply add 1 to current digit (4599 -> 4600)
        digits[i] += 1
        
        return digits