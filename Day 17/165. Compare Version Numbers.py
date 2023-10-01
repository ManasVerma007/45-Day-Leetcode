class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        l1 = len(ver1)
        l2 = len(ver2)
        minimum = min(l1, l2)
        for i in range(minimum):
            int1 = int(ver1[i])
            int2 = int(ver2[i])
            if int1 > int2:
                return 1
            elif int2 > int1:
                return -1
        for i in range(minimum, l1):
            if int(ver1[i]) > 0:
                return 1
        for i in range(minimum, l2):
            if int(ver2[i]) > 0:
                return -1
        return 0  
