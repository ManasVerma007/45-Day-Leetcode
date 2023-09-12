class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sliding_sum = 0
        left = 0
        result = 2**31
        for i in range(len(nums)):
            sliding_sum = sliding_sum + nums[i]
            while sliding_sum >= target:
                subarray_length = i - left + 1
                result = min(result, subarray_length)
                sliding_sum = sliding_sum - nums[left]
                left = left + 1
        if result == 2**31:
            return 0
        else:
            return result
