# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode = []   
        elem_count_dict = {}                     
        
        def find(root):
            if not root:
                return
            
            if root.val in elem_count_dict:
                elem_count_dict[root.val] += 1
            else:
                elem_count_dict[root.val] = 1   
            
            find(root.left)
            find(root.right)
     
        find(root)
        max_elem_count = max(elem_count_dict.values())
        
        for key, value in elem_count_dict.items():
            if value == max_elem_count:
                mode.append(key)
                
        return mode