class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1idx, n2idx, right = m-1, n-1, m+n-1
        while n2idx >= 0:
            if n1idx >= 0 and nums1[n1idx] > nums2[n2idx]:
                nums1[right] = nums1[n1idx]
                n1idx -= 1
            else:
                nums1[right] = nums2[n2idx]
                n2idx -= 1
            right -= 1