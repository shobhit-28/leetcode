class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        if(x < 0):
            x = -x
            negative_checker = True
        else:
            negative_checker = False
        while (x != 0):
            dig = x%10
            num = (num*10) + dig
            x //= 10
        if num >= 2 ** 31 - 1 or num <= -2 ** 31:
            return 0
        else:
            if(negative_checker):
                return (-num)
            else:
                return (num)