# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: 
            return []

        if root.left or root.right:
            return [
                f'{str(root.val)}->{i}' for i in self.binaryTreePaths(root.left)
            ] + [f'{str(root.val)}->{i}' for i in self.binaryTreePaths(root.right)]

        else: 
            return [str(root.val)]    