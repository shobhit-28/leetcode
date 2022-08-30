class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        arr1, arr2 = [], []
        index = 0
        for index in range(0, len(s)):
            for inside_index in range(index, len(s)):
                if s[inside_index] not in arr1:
                    arr1.append(s[inside_index])
                else:
                    arr2.append(arr1)
                    arr1 = []
                    break
        
        for index in range(0, len(arr2)):
            arr2[index] = len(arr2[index])

        arr2.sort()

        return arr2[len(arr2)-1]