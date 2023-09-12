class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash={}
        len=0
        count = 0
        maxres=0
        for i in range(len(nums)):
            if(nums[i]==0):
                count-=1
            else:
                count+=1
            if(count==0):
                len=i+1
                if(len not in hash):
                    hash[i]=1
        for i in hash:
            maxres=max(maxres,i)
        return maxres