class Solution:
    def findComplement(self, num: int) -> int:
        complement_num_str = "".join(['1' if i == '0' else '0' for i in bin(num)[2:]])
        return sum(
            2**power_mul
            for power_mul, i in enumerate(
                range(len(complement_num_str) - 1, -1, -1)
            )
            if int(complement_num_str[i]) == 1
        )