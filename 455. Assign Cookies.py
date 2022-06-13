class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_i = 0
        cookie_i = 0
        
        while cookie_i < len(s) and child_i < len(g):
            if s[cookie_i] >= g[child_i]:
                child_i += 1
            cookie_i += 1
        
        return child_i