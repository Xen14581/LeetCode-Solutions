class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows <= 1 or numRows == len(s) or len(s) == 1:
            return s

        o = ''
        i = 0
        step = 2 * numRows - 2

        while i < numRows:
            j = i
            while j < len(s):
                o += s[j]
                if not i in [0, numRows - 1] and (j + step - 2 * i) < len(s):
                    o += s[j + step - 2 * i]
                j += step
            i += 1

        return o