class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        prefix_sum=0
        result=0
        for i in nums:
            prefix_sum=prefix_sum+i
            if(prefix_sum-k in d):
                result=result+d[prefix_sum-k]
            if(prefix_sum not in d):
                d[prefix_sum]=1
            else:
                d[prefix_sum]+=1
        return result