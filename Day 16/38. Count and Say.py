class Solution:
    def countAndSay(self, n: int) -> str:
        def newstr(st):
            c = 1
            nwstr = ""
            for i in range(len(st)):
                if i < len(st) - 1 and st[i] == st[i + 1]:
                    c += 1
                else:
                    nwstr += str(c) + st[i]
                    c = 1
            return nwstr
        
        if n == 1:
            return '1'
        
        a = '1'
        for _ in range(1, n):
            a = newstr(a)
        
        return a