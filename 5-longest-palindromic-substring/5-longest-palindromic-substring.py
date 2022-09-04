class Solution:
    
    def rev(self, s:str)->str:
        return s[::-1]

    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        front_index = 0
        string = s[front_index]
        while front_index < len(s):
            back_index = len(s)-1
            while back_index > front_index:
                if s[front_index] == s[back_index]:
                    if s[front_index:back_index+1] == Solution.rev(Solution, s[front_index:back_index+1]):
                        if len(string) < len(s[front_index:back_index+1]):
                            string = s[front_index:back_index+1]
                back_index = back_index - 1
            front_index = front_index + 1
        return string