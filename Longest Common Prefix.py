class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        strs.sort()
        o = ''
        for i, j in zip(strs[0], strs[-1]):
            if i == j: o+=i
            else: break
        return o