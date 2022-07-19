class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        freq_list = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            count_dict[i] = 1 + count_dict.get(i, 0)
        
        for num, count in count_dict.items():
            freq_list[count].append(num)
        
        res = []
        
        for i in range(len(freq_list) - 1, 0, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) == k:
                    return res