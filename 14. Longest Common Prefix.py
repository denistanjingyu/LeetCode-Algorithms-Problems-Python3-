class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Return empty string if array is empty
        if not strs:
            return ""
        
        # Get the shortest word as it is the longest common prefix possible
        shortest_word = min(strs, key = len)
        
        # Outer for loop through index and character of shortest word
        for idx, char in enumerate(shortest_word):
            # Inner for loop through each word in array
            for word in strs:
                # Once any character doesn't match, return truncated shortest word
                if word[idx] != char:
                    return shortest_word[:idx]
        
        # If for loop didn't return, means all match. Then return entire shortest word.
        return shortest_word