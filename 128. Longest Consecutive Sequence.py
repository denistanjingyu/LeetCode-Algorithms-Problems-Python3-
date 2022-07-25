class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Set to verify start of sequence and consecutive element (if any)
        hashset = set(nums)
        
        # Variable to store the length of the longest consecutive elements sequence
        longest = 0
        
        # Loop through nums to find out longest consecutive elements sequence
        for integer in nums:
            if integer - 1 not in hashset:
                seq_len = 0
                
                while integer + seq_len in hashset:
                    seq_len += 1
                
                longest = max(seq_len, longest)
        
        return longest