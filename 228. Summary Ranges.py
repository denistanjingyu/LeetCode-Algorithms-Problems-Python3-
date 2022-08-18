class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        for i in nums:
            if res and res[-1][1] == i-1:
                res[-1][1] = i
            else:
                res.append([i, i])

        return [f"{str(x)}->{str(y)}" if x != y else str(x) for [x, y] in res]