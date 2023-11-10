class Solution:
    def NBitBinary(self, n):
        res = []
        self.generate_numbers(n, res=res, one=0, zero=0)
        return res

    def generate_numbers(self, n, num='', res=None, one=0, zero=0):
        if res is None:
            res = []
            one = 0
            zero = 0

        if n == 0:
            if one >= zero:
                if(num[0]!='0'):
                    res.append(num)
        else:
            self.generate_numbers(n - 1, num + '1', res, one + 1, zero)
            self.generate_numbers(n - 1, num + '0', res, one, zero + 1)

        return res