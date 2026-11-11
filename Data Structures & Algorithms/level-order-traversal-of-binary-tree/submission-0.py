# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, nl = [[root.val]], [[root]]
        while len(res[-1]) > 0:
            nl.append([])
            res.append([])
            for node in nl[-2]:
                if node.left:
                    nl[-1].append(node.left)
                    res[-1].append(node.left.val)
                if node.right:
                    nl[-1].append(node.right)
                    res[-1].append(node.right.val)
        res.pop()
        return res