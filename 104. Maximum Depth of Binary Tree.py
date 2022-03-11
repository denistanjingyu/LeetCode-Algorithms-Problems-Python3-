# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive solution to travel down every single path
        # Base case: left or right node is empty
        # Add 1 to depth for every node down the path
        def find_depth(root, depth):
            if not root:
                return depth
            else:
                return max(find_depth(root.left, depth+1), find_depth(root.right, depth+1))
        
        return find_depth(root, 0)