class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        original_a = a
        count = 1

        while len(a) < len(b):
            a += original_a
            count += 1

        if b in a:
            return count

        a += original_a
        count += 1

        if b in a:
            return count

        return -1