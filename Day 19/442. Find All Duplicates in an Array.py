class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for num in nums:
            index = abs(num) - 1  
            
            if nums[index] < 0:
                duplicates.append(index + 1)   
            else:
                nums[index] = -nums[index] 
        
        for i in range(len(nums)):
            nums[i] = abs(nums[i])  
        
        return duplicates

#(Above approach is O(n) time and O(1) space)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num_count = {}
        duplicates = []

        for num in nums:
            if num in num_count:
                duplicates.append(num)
            else:
                num_count[num] = 1

        return duplicates

# the above approach is O(n) time and O(n) space