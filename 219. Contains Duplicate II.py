class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for idx, value in enumerate(nums):
            if value in dic and idx - dic[value] <= k:
                return True
            dic[value] = idx
        return False