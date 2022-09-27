class Solution:
    def isPalindrome(self, num: int) -> bool:
        new_num1 = num
        new_num2 = 0
        while(new_num1 > 0):
            digit = new_num1 % 10
            new_num2 = (new_num2*10) + digit
            new_num1 //= 10
        check = (num == new_num2)
        return(check)