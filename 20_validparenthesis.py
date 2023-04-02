p = []
last = ""
s = "()[]"


for i, val in enumerate(s):
    if val in "({[":
        p.append(val)
        result = False
        continue
    
    if(len(p) != 0):
        last = p[-1]
    if ((val == ")" and last == "(") or
        (val == "}" and last == "{") or
        (val == "]" and last == "[")):
        p.pop()
        last = ""
    else:
        result = False
        break
    
if len(p) == 0:
    result = True

print(result)


"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store = {"(":")", "{": "}", "[": "]"}

        for elem in s:
            if elem in store:
                stack.append(elem)
            else:
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if elem != store[item]:
                    return False
        
        return len(stack) == 0
            


"""


"""

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                temp = stack.pop()
                if temp != dic[c]:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

"""


"""
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        data = {
            '(':')',
            '{':'}',
            '[':']'
        }
        
        stack = []
        for char in list(s):
            if char in data:
                stack.append(char)
            elif stack and data[stack.pop()] == char:
                continue
            else:
                return False
        
        return not stack

"""


