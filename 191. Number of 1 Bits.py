class Solution:
    def hammingWeight(self, n: int) -> int:
        return "{0:032b}".format(n).count('1')