class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for num in matrix:
            nums = nums + num
        nums.sort()
        return nums[(k-1)]