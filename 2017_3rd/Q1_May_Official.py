class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = version1.split('.')
        l2 = version2.split('.')
        
        len1 = len(l1)
        len2 = len(l2)
        
        if len1 >= len2:
            l2.extend([0]*(len1-len2))
        else:
            l1.extend([0]*(len2-len1))
        
        for i in range(len(l1)):
            if int(l1[i])>int(l2[i]):
                return 1
            elif int(l1[i])==int(l2[i]):
                continue
            else:
                return -1
        
        return 0
        
if __name__ == '__main__':
	sol = Solution()
	v1,v2 = raw_input().split()
	print sol.compareVersion(v1,v2)
