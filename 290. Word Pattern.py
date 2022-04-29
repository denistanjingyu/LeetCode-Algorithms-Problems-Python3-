class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        w_to_p = {}

        if len(pattern) != len(words):
            return False
        
        # For the case w = ['dog', 'cat'] and p = 'aa'
        if len(set(pattern)) != len(set(words)):
            return False 

        for word, letter in zip(words, pattern):
            if word not in w_to_p: 
                w_to_p[word] = letter
            elif w_to_p[word] != letter: 
                return False

        return True