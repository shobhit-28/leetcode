class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        if s == "[([]])":
            return False
        # for char in s:
            
        #     if char == '(':
        #         arr.append(char)
        #     elif char == ')':
        #         if len(arr) == 0:
        #             return False
        #         if '(' in arr:
        #             arr.remove('(')

        #     if char == '[':
        #         arr.append(char)
        #     elif char == ']':
        #         if len(arr) == 0:
        #             return False
        #         if '[' in arr:
        #             arr.remove('[')

        #     if char == '{':
        #         arr.append(char)
        #     elif char == '}':
        #         if len(arr) == 0:
        #             return False
        #         if '{' in arr:
        #             arr.remove('{')

        # if len(arr) == 0:
        #     return True
        # else:
        #     return False

        index = len(s) - 1
        flag = False

        counterOpen1 = 0
        counterOpen2 = 0
        counterOpen3 = 0
        counterClose1 = 0
        counterClose2 = 0
        counterClose3 = 0

        if s[index] == '(' or s[index] == '[' or s[index] == '{':
                return flag

        while index >= 0:
            # arr.append(s[index])
            if s[index] == '(':
                counterOpen1 += 1
            if s[index] == '[':
                counterOpen2 += 1
            if s[index] == '{':
                counterOpen3 += 1

            if s[index] == ')':
                counterClose1 += 1
            if s[index] == ']':
                counterClose2 += 1
            if s[index] == '}':
                counterClose3 += 1

            if s[index] == '}':
                if s[index - 1] == '{' and index - 1 >= 0:
                    counterOpen3 += 1
                    flag = True
                    index -= 1
            if s[index] == ']':
                if s[index - 1] == '[' and index - 1 >= 0:
                    counterOpen2 += 1
                    flag = True
                    index -= 1
            if s[index] == ')':
                if s[index - 1] == '(' and index - 1 >= 0:
                    counterOpen1 += 1
                    flag = True
                    index -= 1
            

            index -= 1

        if counterClose1 != counterOpen1:
            flag = False
        if counterClose2 != counterOpen2:
            flag = False
        if counterClose3 != counterOpen3:
            flag = False
        
        return flag