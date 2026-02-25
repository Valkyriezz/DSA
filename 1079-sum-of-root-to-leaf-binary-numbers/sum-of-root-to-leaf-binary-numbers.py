# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # binaries=[]
        # curr=""
        summ=0
        curr=0
        def dfs(root,curr):
            nonlocal summ
            if root is None:
                return 
            curr=curr*2+root.val
            if root.left is None and root.right is None:
                summ+=curr
                return
            dfs(root.left,curr)
            dfs(root.right,curr)
        dfs(root,curr)
        # for i in binaries:
        #     summ+=int(i,2)
        return summ


# 2 5 -> 25
# 2
# 2 * 10 + 5
# currbit * 2 + bit

# bit -> 1.  sum ->1
# sum * 2 + bit
# currsum * 10 + num

# 10
# 1 * 2 + 0 = 2


        