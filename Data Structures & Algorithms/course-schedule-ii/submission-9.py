class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: set() for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].add(pre)
        
        visited, cycle = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if not crs in visited and len(preMap[crs]) == 0:
                res.append(crs)
                visited.add(crs)
                return True
            
            cycle.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs].clear()
            cycle.remove(crs)
            if not crs in visited: res.append(crs)
            visited.add(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res