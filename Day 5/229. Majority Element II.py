class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elem1 = 0
        elem2 = 0
        count1 = 0
        count2 = 0
        
        for i in nums:
            if count1 == 0 and i != elem2:
                elem1 = i
                count1 = 1
            elif count2 == 0 and i != elem1:
                elem2 = i
                count2 = 1
            elif i == elem1:
                count1 += 1
            elif i == elem2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        result = []
        if nums.count(elem1) > len(nums) // 3:
            result.append(elem1)
        if elem1 != elem2 and nums.count(elem2) > len(nums) // 3:
            result.append(elem2)
        
        return result
