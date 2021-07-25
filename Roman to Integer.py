class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        if len(s) == 1:
            return d[s[0]]

        l = len(s) - 1
        o = 0

        for i in range(l, -1, -1):
            if i != l and s[i] == 'I' and (s[i + 1] in ['V', 'X']):
                o -= 1
            elif i != l and s[i] == 'X' and (s[i + 1] in ['L', 'C']):
                o -= 10
            elif i != l and s[i] == 'C' and (s[i + 1] in ['D', 'M']):
                o -= 100
            else:
                o += d[s[i]]

        return o
