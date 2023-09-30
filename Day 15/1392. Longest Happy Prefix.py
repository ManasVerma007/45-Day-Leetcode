class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        longest_common = ""
        
        for i in range(1, n):
            prefix = s[:i]
            suffix = s[-i:]
            
            if prefix == suffix:
                longest_common = prefix
        
        return longest_common
