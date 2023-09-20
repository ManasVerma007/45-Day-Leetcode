class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s[::-1]
        result = ""
        t = ""
        sc = 0
        for i in range(len(s)):
            if s[i] == " ":
                sc += 1
                if sc == 1:
                    t = t[::-1]
                    result += t + " "
                    t = ""
            else:
                t += s[i]
                sc = 0
        
        # Add the last word (if any) to the result
        if t:
            result += t[::-1]
        
        return result