class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert all uppercase letters into lowercase letters
        s = s.lower()
        
        # Remove all non-alphanumeric characters
        for char in s:
            if not char.isalnum():
                s = s.replace(char, "")
        
        # Check whether it reads the same forward and backward
        return s == s[::-1]