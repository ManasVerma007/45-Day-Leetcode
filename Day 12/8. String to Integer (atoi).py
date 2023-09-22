class Solution:
    def myAtoi(self, s):
        # Initialize pointers and constants
        i = 0
        n = len(s)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Initialize sign counters
        positive_signs = 0
        negative_signs = 0

        # Count positive signs at the start of the string
        if i < n and s[i] == '+':
            positive_signs += 1
            i += 1

        # Count negative signs at the start of the string
        if i < n and s[i] == '-':
            negative_signs += 1
            i += 1

        # Initialize the result
        result = 0.0

        # Convert characters to an integer
        while i < n and '0' <= s[i] <= '9':
            result = result * 10 + (ord(s[i]) - ord('0'))
            i += 1

        # Apply signs
        if negative_signs > 0:
            result = -result

        # Check for both positive and negative signs
        if positive_signs > 0 and negative_signs > 0:
            return 0

        # Handle overflow and underflow
        if result > INT_MAX:
            result = INT_MAX

        if result < INT_MIN:
            result = INT_MIN

        return int(result)
