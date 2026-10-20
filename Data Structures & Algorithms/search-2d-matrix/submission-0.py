class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) * len(matrix[0]) - 1
        while i <= j:
            mid = (i + j) // 2
            midi = mid // len(matrix[0])
            midj = mid % len(matrix[0])
            if matrix[midi][midj] == target:
                return True
            elif matrix[midi][midj] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False