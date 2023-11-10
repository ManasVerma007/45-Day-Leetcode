class Solution:
    def NBitBinary(self, n):
        res = []  # Create an empty list to store results
        final=self.generate_numbers(n, res=res)  # Call the method with the list as an argument
        return final
    def generate_numbers(self, n, num='', res=None):
        if res is None:
            res = []  # Initialize res as an empty list if not provided

        if n == 0:
            res.append(num)
        else:
            for digit in ['0', '1']:
                if num and num[-1] == '1' and digit == "1":
                    pass
                else:
                    self.generate_numbers(n - 1, num + digit, res)

        return res  # Return the list of generated numbers