class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1

        mydict = {}
        maxc = 0
        c = 0
        left_ptr = 0

        for right_ptr, char in enumerate(s):
            if char not in mydict:
                mydict[char] = True
                c += 1
            else:
                maxc = max(maxc, c)
                while s[left_ptr] != char:
                    del mydict[s[left_ptr]]
                    left_ptr += 1
                    c -= 1
                left_ptr += 1

        return max(maxc, c)

