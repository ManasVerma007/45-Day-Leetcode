from typing import List
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort(reverse=True)
        res = 0
        n, m = len(nums), len(nums[0])
        for i in range(m):
            curr_max = -1  
            for j in range(n):
                curr_max = max(curr_max, nums[j][i])  
            res += curr_max          
        return res