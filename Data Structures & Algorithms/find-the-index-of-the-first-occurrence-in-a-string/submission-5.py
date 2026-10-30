class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Given strings
        # use string.find('substring')
        n, m = len(haystack), len(needle)

        i = 0
        while i <= n - m:
            tmp = haystack[i: i + m]
            for j in range(m):
                if tmp[j] != needle[j]:
                    break
            
            else:
                return i
                    
            i += 1
        return -1
        