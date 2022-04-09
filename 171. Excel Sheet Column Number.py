class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Convert base 26 to base 10
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter) - 64
            ans += digit * 26**pos
            pos += 1
            
        return ans    