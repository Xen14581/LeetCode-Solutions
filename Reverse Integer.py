class Solution:
    def reverse(self, x: int) -> int:
        r=int(str(abs(x))[::-1])
        if r <= -2147483648 or r >= 2147483647:
            return 0
        if x < 0:
            return -r
        return r