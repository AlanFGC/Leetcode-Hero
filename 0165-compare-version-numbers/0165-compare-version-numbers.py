class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        If version1 < version2, return -1.
        If version1 > version2, return 1.
        Otherwise, return 0.
        """
        lv1 = version1.split(".")
        lv2 = version2.split(".")
        
        i = 0
        j = 0
        
        
        v1 = int(lv1[i])
        v2 = int(lv2[j])
        while True:
            
            if v1 > v2:
                return 1
            elif v2 > v1:
                return -1
            
            # select next v1
            if i < len(lv1)-1:
                i += 1
                v1 = int(lv1[i])
            else:
                v1 = 0
            
            # select next v2
            if j < len(lv2)-1:
                j += 1
                v2 = int(lv2[j])
            else:
                v2 = 0
            
            
            
            if i == len(lv1) - 1 and j == len(lv2) - 1 and v1 == v2:
                return 0