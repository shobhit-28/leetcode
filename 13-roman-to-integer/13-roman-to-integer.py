class Solution:
    def romanToInt(self, s: str) -> int:
        arr = [*s]
        val = 0
        char = len(arr)-1
        while char >= 0:
            if arr[char] == 'I':
                val += 1
                if arr[char - 1] == 'I' and char-1 > -1:
                    val += 1
                    char -= 1
                    if arr[char - 1] == 'I' and char-1 > -1:
                        val += 1
                        char -= 1
            elif arr[char] == 'V':
                val += 5
                if arr[char - 1] == 'I' and char-1 > -1:
                    val -= 1
                    char -= 1
            elif arr[char] == 'X':
                val += 10
                if arr[char - 1] == 'I' and char-1 > -1:
                    val -= 1
                    char -= 1
                if arr[char - 1] == 'X' and char-1 > -1:
                    val += 10
                    char -= 1
                    if arr[char - 1] == 'X' and char-1 > -1:
                        val += 10
                        char -= 1
            elif arr[char] == 'L':
                val += 50
                if arr[char - 1] == 'X' and char-1 > -1:
                    val -= 10
                    char -= 1
            elif arr[char] == 'C':
                val += 100
                if arr[char - 1] == 'X' and char-1 > -1:
                    val -= 10
                    char -= 1
            elif arr[char] == 'D':
                val += 500
                if arr[char - 1] == 'C' and char-1 > -1:
                    val -= 100
                    char -= 1
            elif arr[char] == 'M':
                val += 1000
                if arr[char - 1] == 'C' and char-1 > -1:
                    val -= 100
                    char -= 1
    
            char -= 1
    
        return val 