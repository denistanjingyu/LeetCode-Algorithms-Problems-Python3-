class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result_set = {}

        for idx, i in enumerate(numbers):
            if target - i in result_set:
                return [result_set[target - i], idx + 1]

            result_set[i] = idx + 1