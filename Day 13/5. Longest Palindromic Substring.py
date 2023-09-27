class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1  # Needle is longer than haystack, so no match is possible
        
        if not needle:
            return 0  # Return 0 if the needle is an empty string
        # Create a mapping of characters to values for the rolling hash
        d = {}
        k = 1
        for char in set(haystack + needle):
            d[char] = k
            k += 1
        # Compute the hash of the needle
        check_val = 0
        k = 0
        for i in range(len(needle) - 1, -1, -1):
            char = needle[i]
            if char not in d:
                return -1  # Character not in the mapping
            check_val = check_val + (d[char] * (10 ** k))
            k += 1
        
        # Initialize the rolling hash value
        rolling_hash = 0
        k = len(needle)
        for i in range(len(needle)):
            char = haystack[i]
            if char not in d:
                return -1  # Character not in the mapping
            rolling_hash = rolling_hash + (d[char] * (10 ** (k - 1)))
            k -= 1

        # Check the first window
        if rolling_hash == check_val:
            return 0
        
        # Iterate through the haystack using a rolling hash
        for i in range(1, len(haystack) - len(needle) + 1):
            # Update the rolling hash
            char_to_remove = haystack[i - 1]
            char_to_add = haystack[i + len(needle) - 1]
            
            if char_to_remove not in d or char_to_add not in d:
                return -1  # Character not in the mapping
            
            rolling_hash = (rolling_hash - d[char_to_remove] * (10 ** (len(needle) - 1))) * 10 + d[char_to_add]

            if rolling_hash == check_val:
                return i

        return -1  # If no match is found, return -1