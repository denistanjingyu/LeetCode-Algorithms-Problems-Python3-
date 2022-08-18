class Solution:
    def isHappy(self, n: int) -> bool:
        memory_set = set()
        while n not in memory_set:
            memory_set.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1