class Solution:
    def searchMatrix(self, A: List[List[int]], target: int) -> bool:
        if A[0][0] == target:
            return True
        
        rows = len(A)
        cols = len(A[0])
        top = 0
        bottom = rows - 1
        
        if rows == 1:
            left = 0
            right = cols - 1
            while left <= right:
                mid = left + (right - left) // 2
                if A[0][mid] == target:
                    return True
                elif A[0][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        while top < bottom:
            mid = top + (bottom - top) // 2
            
            if A[mid][cols - 1] == target:
                return True
            elif target < A[mid][cols - 1]:
                bottom = mid
            else:
                top = mid + 1
        
        left = 0
        right = cols - 1
        while left <= right:
            mid = left + (right - left) // 2
            if A[top][mid] == target:
                return True
            elif A[top][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
