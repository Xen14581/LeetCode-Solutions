class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 + nums2
        a.sort()
        l = len(a)
        i = int(l/2)
        if l % 2:
            return a[i]
        else:
            return (a[i]+a[i-1])/2