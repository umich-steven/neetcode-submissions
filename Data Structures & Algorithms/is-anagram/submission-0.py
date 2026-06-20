class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}
        for i in sorted(s):
            if i not in s_table:
                s_table[i] = 1
            else:
                s_table[i] += 1
        for i in sorted(t):
            if i not in t_table:
                t_table[i] = 1
            else:
                t_table[i] += 1
        if s_table == t_table:
            return True
        else:
            return False