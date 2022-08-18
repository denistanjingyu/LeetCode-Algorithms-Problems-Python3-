class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_sorted_list = sorted(list(set(nums)))

        if len(distinct_sorted_list) < 3:
            return max(distinct_sorted_list)
        else:
            return distinct_sorted_list[-3]