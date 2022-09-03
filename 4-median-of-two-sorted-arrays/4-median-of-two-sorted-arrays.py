class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        if len(arr)%2 != 0:
            return arr[(len(arr)//2)]
        else:
            a =len(arr)//2
            res = (arr[a] + arr[a-1])/2
            return res