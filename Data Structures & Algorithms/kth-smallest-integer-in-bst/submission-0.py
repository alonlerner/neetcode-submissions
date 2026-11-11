# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(r, a):
            if r:
                dfs(r.left, a)
                a.append(r.val)
                dfs(r.right, a)
        a = []
        dfs(root, a)
        return a[k-1]