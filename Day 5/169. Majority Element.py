class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ans=0
        count=0
        for i in nums:
            if(count==0):
                ans=i
            if(i==ans):
                count=count+1
            else:
                count=count-1
        return ans
#         a = {}
#         max_count = 0
#         majority_num = None
        
#         for num in nums:
#             if num in a:
#                 a[num] += 1
#             else:
#                 a[num] = 1
            
#             if a[num] > max_count:
#                 max_count = a[num]
#                 majority_num = num
        
#         return majority_num
