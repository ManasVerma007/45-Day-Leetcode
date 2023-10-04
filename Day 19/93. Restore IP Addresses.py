from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            return 0 <= int(segment) <= 255 and (len(segment) == 1 or segment[0] != '0')
        n = len(s)
        valid_ip_addresses = []
        for i in range(1, min(4, n - 2)):
            for j in range(i + 1, min(i + 4, n - 1)):
                for k in range(j + 1, min(j + 4, n)):
                    segment1, segment2, segment3, segment4 = s[:i], s[i:j], s[j:k], s[k:]
                    if is_valid(segment1) and is_valid(segment2) and is_valid(segment3) and is_valid(segment4):
                        valid_ip = f"{segment1}.{segment2}.{segment3}.{segment4}"
                        valid_ip_addresses.append(valid_ip)
        return valid_ip_addresses
