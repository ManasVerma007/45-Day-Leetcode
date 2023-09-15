class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set for faster lookup
        num_set = set(nums)
        
        longest_streak = 0
        
        # Iterate through the numbers
        for num in num_set:
            # Check if the current number is the start of a streak
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Continue incrementing the number to find the streak length
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak if necessary
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
