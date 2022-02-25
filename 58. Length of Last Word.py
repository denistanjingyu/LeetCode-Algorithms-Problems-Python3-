class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Define a variable to store length of last word to be returned
        len_of_last_word = 0
        
        # Define a variable to point to last index of given string
        i = len(s) - 1
        
        # Define a variable that is False until the first character appears
        found_a_char = False
        
        # Loop continues if current character is not a space or first character is not found
        # Add 1 count to len_of_last_word if current character is not a space
        # found_a_char becomes true at first occurrence of a non-space
        # Decrease i by 1 to move to the next character (to the left in this case)
        # Since 1st index is 0, break if index < 0 to avoid out of range error
        while s[i] != " " or not found_a_char:
            if s[i] != " ":
                len_of_last_word += 1
                found_a_char = True
            i -= 1
            if i < 0:
                break
        
        return len_of_last_word