class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            row = top + (bot - top) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not top <= bot:
            return False

        row = top + (bot - top) // 2
        left, right = 0, cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
        
        return False