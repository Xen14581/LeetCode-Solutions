class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        ss = ''

        for c in s:
            if c not in ss:
                ss += c
            else:
                ss = ss[ss.index(c) + 1:] + c
            l = max(l, len(ss))
        return l
