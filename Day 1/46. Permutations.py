class Solution:
    def permute(self, nums):
        permutations = []
        
        self.dfs(nums, [], permutations)
        return permutations

    def dfs(self, nums, current_permutation, permutations):
        if not nums:
            permutations.append(current_permutation)
            return
        
        # Iterate through each element in nums
        for i in range(len(nums)):
            # Choose an element
            chosen = nums[i]
            
            # Create a copy of the current_permutation and add the chosen element
            new_permutation = current_permutation + [chosen]
            
            # Create a copy of nums without the chosen element
            remaining_nums = nums[:i] + nums[i+1:]
            
            # Recursively explore with the new_permutation and remaining_nums
            self.dfs(remaining_nums, new_permutation, permutations)
