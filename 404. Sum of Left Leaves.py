# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeft = False) -> int:
            if not root: 
                return 0
            
            if not (root.left or root.right): 
                return root.val * isLeft
            
            return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)