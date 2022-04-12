class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mem = {}
        
        for i in range(len(s)):
            if s[i] not in mem:
                mem[s[i]] = t[i]
            if t[i] != mem[s[i]]:
                return False
        
        check_list = [[k, v] for k, v in mem.items()]
        check_dup_list = [pair[1] for pair in check_list]
        check_dup_set = set(check_dup_list)
        
        return len(check_dup_list) == len(check_dup_set)