# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(r, x, a):
            if root:
                a.append(r)
                if r != x:
                    if r.val > x.val:
                        helper(r.left, x, a)
                    else:
                        helper(r.right, x, a)
        a1, a2 = [], []
        helper(root, p, a1)
        helper(root, q, a2)
        i = 0
        while i < len(a1) and i < len(a2) and a1[i] == a2[i]:
            i += 1
        return a1[i-1]