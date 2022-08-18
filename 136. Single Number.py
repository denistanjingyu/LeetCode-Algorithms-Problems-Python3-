class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_nums = {}
        for i in nums:
            if i not in dict_nums:
                dict_nums[i] = 1
            else:
                dict_nums[i] += 1

        for num, count in dict_nums.items():
            if count == 1:
                return num