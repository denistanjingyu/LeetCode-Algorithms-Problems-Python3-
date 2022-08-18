class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if not s:
            return True

        subsequence = 0

        for i in range(len(t)):
            if subsequence <= len(s) - 1 and s[subsequence] == t[i]:
                subsequence += 1

        return  subsequence == len(s)