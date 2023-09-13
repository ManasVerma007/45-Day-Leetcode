class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        A.sort()
        result = []
        for interval in A:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
