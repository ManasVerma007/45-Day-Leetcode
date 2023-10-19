class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(remaining, current, start):
            if len(current) == k:
                results.append(current[:])
                return

            for i in range(start, n + 1):
                current.append(i)
                backtrack(remaining - 1, current, i + 1)
                current.pop()

        results = []
        backtrack(k, [], 1)
        return results