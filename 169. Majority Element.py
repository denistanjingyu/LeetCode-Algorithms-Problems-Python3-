class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Dictionary method
        res = {}
        for elem in nums:
            if elem not in res:
                res[elem] = 1
            else:
                res[elem] += 1
        
        major_elem = [elem for elem, count in res.items() if (count > len(nums)/2)][0]
        return major_elem