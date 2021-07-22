class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        i = 0

        if not len(s):
            return 0

        neg = s[0] == '-'
        pos = s[0] == '+'

        if len(s) > 0 and (neg or pos):
            i += 1

        n = 0

        while i < len(s) and '0' <= s[i] <= '9':
            n = 10 * n + int(s[i])
            i += 1

        if neg:
            n = -n

        if n < -2147483648:
            return -2147483648
        if n > 2147483647:
            return 2147483647
        return n

