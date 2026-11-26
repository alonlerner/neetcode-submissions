class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {i+1: i+1 for i in range(len(edges))}
        rank = {i+1: 1 for i in range(len(edges))}

        def find(n):
            while par[n] != n:
                n = par[n]
            return n
        
        def union(edge):
            n1, n2 = edge[0], edge[1]
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for edge in edges:
            if not union(edge):
                return edge
