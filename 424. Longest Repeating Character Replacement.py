class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_count = {}
        longest_substr = 0
        
        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            
            while (r - l + 1) - max(char_count.values()) > k:
                char_count[s[l]] -= 1
                l += 1
                
            longest_substr = max(longest_substr, r - l + 1)
            
        return longest_substr