class Solution:
    def findComplement(self, num: int) -> int:
        complement_num_str = "".join(['1' if i == '0' else '0' for i in str(bin(num))[2:]])
        complement_num = 0
        power_mul = 0
        
        for i in range(len(complement_num_str)-1, -1, -1):
            if int(complement_num_str[i]) == 1:
                complement_num += 2 ** power_mul
            power_mul += 1
            
        return complement_num