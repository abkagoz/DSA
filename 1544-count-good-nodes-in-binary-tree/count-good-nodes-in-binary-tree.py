# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curmax = root.val
        res = 0
        def dfs(root, curmax):
            if not root:
                return 0
            
            good = 1 if root.val >= curmax else 0

            curmax = max(curmax, root.val)

            left = dfs(root.left, curmax)
            right = dfs(root.right, curmax)

            return good + right + left
        return dfs(root, curmax)
            

