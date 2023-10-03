class Solution:
    def reverse(x: int) -> int:
    # Define maximum and minimum integer values
        MAX_INT = 2 ** 31 - 1 :
        MIN_INT = -2 ** 31    

        # Initialize the reversed number
        reversed_num = 0

        # Handle the sign of the input
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x > 0:
            # Extract the last digit
            last_digit = x % 10

            # Check for potential overflow
            if reversed_num > (MAX_INT - last_digit) // 10:
                return 0

            # Add the last digit to the reversed number
            reversed_num = reversed_num * 10 + last_digit

            # Remove the last digit from the input
            x //= 10

        # Apply the sign to the reversed number
        reversed_num *= sign

        return reversed_num

        