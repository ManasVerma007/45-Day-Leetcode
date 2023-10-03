class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1 
        MIN_INT = -2 ** 31    
        reversed_num = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            last_digit = x % 10
            if reversed_num > (MAX_INT - last_digit) // 10:
                return 0
            reversed_num = reversed_num * 10 + last_digit
            x //= 10
        reversed_num *= sign
        return reversed_num
