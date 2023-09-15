class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums),1):
                diff=target-(nums[i]+nums[j])
                start=j+1
                end=len(nums)-1
                while(start<end):
                    if(nums[start]+nums[end]<diff):
                        start=start+1
                    elif(nums[start]+nums[end]>diff):
                        end=end-1
                    else:
                        res.append((nums[i],nums[j],nums[start],nums[end]))
                        start=start+1
                        end=end-1
        return set(res)