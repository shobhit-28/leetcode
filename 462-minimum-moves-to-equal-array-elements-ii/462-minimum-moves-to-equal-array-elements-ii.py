class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        movesCounter = 0
        targetNum = nums[len(nums)//2]
        for num in nums:
            movesCounter += abs(targetNum - num)
        return movesCounter