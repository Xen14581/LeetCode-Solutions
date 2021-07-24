class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        o = 0

        while i < j:

            if height[i] <= height[j]:
                r = height[i] * (j - i)
                if r > o:
                    o = r
                i += 1
            else:
                r = height[j] * (j - i)
                if r > o:
                    o = r
                j -= 1

        return o