class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2 = nums[n:]
        nums1 = nums[:n]
        nums = []
        for num in range(0,n):
            nums.append(nums1[num])
            nums.append(nums2[num])
        return nums