class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        complete_set = {i + 1 for i in range(len(nums))}
        given_set = set(nums)

        return list(complete_set - given_set)