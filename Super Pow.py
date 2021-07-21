class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        i = ''
        for num in b:
            i += str(num)
        i = int(i)
        return pow(a, i, 1337)