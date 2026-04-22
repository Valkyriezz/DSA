# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # expand every node and checking 
        maximumdia=0
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        def expand(node):
            nonlocal maximumdia 
            if not node:
                return 0
            left=expand(node.left)
            right=expand(node.right)
            maximumdia=max(maximumdia,left+right)
            return 1+max(left,right)
        expand(root)
        return maximumdia
