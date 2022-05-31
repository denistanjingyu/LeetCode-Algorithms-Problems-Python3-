class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        dict_s, dict_t = {}, {}
        
        for char in s:
            if char not in dict_s:
                dict_s[char] = 1
            else:
                dict_s[char] += 1

        for char in t:
            if char not in dict_t:
                dict_t[char] = 1
            else:
                dict_t[char] += 1
        
        set_s = set(dict_s.items())
        set_t = set(dict_t.items())
        symm_diff = set_s ^ set_t
        
        res = list(symm_diff)[0][0]
        
        return res