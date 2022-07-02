class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        single_row_words = []
        
        for word in words:
            if set(word.lower()).issubset(set(first_row)) or set(word.lower()).issubset(set(second_row)) or set(word.lower()).issubset(set(third_row)):
                single_row_words.append(word)
        
        return single_row_words