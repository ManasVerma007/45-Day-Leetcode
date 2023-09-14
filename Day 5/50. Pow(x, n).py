class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(base=x, exp=abs(n)):
            if(exp==0):
                return 1
            elif(exp%2==0):
                return power(base*base, exp//2)
            else:
                return base*power(base*base, (exp-1)//2)
        f = power()
        if (n>=0):
            return float(f)
        else:
            return 1/f