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
        q = deque[node]
        visited = set()
        nodeMap = {node: res}

        def dfs(n, nn):
            visited.add(n)
            for neighbor in n.neighbors:
                if not neighbor in visited:
                    newNeighbor = Node(neighbor.val)
                    nodeMap[neighbor] = newNeighbor
                    dfs(neighbor, newNeighbor)
                else:
                    newNeighbor = nodeMap[neighbor]
                nn.neighbors.append(newNeighbor)
        dfs(node, res)
        return res
