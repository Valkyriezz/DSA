# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        binaries=[]
        curr=""
        def dfs(root,curr):
            if root is None:
                return 
            curr+=str(root.val)
            if root.left is None and root.right is None:
                binaries.append(curr)
                return
            dfs(root.left,curr)
            dfs(root.right,curr)
        dfs(root,curr)
        summ=0
        for i in binaries:
            summ+=int(i,2)
        return summ


        