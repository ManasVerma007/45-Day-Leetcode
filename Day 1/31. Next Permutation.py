class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums) - 1

        # Find the first element from the right that is smaller than the element next to it
        while i > 0 and nums[i - 1] >= nums[i]:
            i = i - 1

        if i == 0:
            # If no such element is found, reverse the whole list
            nums.reverse()
            return

        # Find the smallest element in nums[j:] that is greater than nums[i-1]
        while nums[j] <= nums[i - 1]:
            j = j - 1

        # Swap nums[i-1] and nums[j]
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Reverse the subarray nums[i:] to get the smallest permutation
        nums[i:] = nums[len(nums) - 1 : i - 1 : -1]
