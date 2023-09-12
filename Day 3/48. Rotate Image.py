class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)  # Get the size of the matrix (assumes it's a square matrix)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                # Swap elements at (i, j) and (j, i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        left, right = 0, n - 1  # Initialize pointers for flipping columns
        
        # Step 2: Flip the matrix horizontally (rotate 90 degrees clockwise)
        while left < right:
            for i in range(n):
                # Swap elements in the same row but at columns 'left' and 'right'
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
