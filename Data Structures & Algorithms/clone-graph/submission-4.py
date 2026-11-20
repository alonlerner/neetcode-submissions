"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        res = Node(node.val)
        nodeMap = {node: res}
        q = deque()
        q.append(node)
        while q:
            curNode = q.popleft()
            newNode = nodeMap[curNode]
            for n in curNode.neighbors:
                if not n in nodeMap:
                    nodeMap[n] = Node(n.val)
                    q.append(n)
                newNode.neighbors.append(nodeMap[n])
        return res
