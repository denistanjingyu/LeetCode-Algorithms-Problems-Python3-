class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_store = {}
        res = []

        for i in nums1:
            if i not in dict_store:
                dict_store[i] = 1
            else:
                dict_store[i] += 1

        for j in nums2:
            if j in dict_store and dict_store[j] > 0:
                res.append(j)
                dict_store[j] -= 1

        return res