class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_list_of_str = list(magazine)
        char_store = {}

        for char in mag_list_of_str:
            if char not in char_store:
                char_store[char] = 1
            else:
                char_store[char] += 1

        for note_char in ransomNote:
            if note_char not in char_store or char_store[note_char] == 0:
                return False
            else:
                char_store[note_char] -= 1

        return True