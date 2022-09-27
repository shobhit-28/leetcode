class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                currNum = num
                currLen = 1
                while currNum + 1 in nums:
                    currNum += 1
                    currLen += 1
                maxLen = max(currLen, maxLen)
        return maxLen