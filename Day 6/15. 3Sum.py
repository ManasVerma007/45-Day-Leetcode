from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, elem in enumerate(nums):
            if i > 0 and elem == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if elem + nums[l] + nums[r] == 0:
                    res.append([elem, nums[l], nums[r]])
                    l = l + 1
                    while nums[l] == nums[l - 1] and l < r:
                        l = l + 1
                elif elem + nums[l] + nums[r] < 0:
                    l = l + 1
                else:
                    r = r - 1
        return res
