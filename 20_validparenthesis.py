p = []
last = ""
s = "[({})[]}]"


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


"""

class Solution:
    def isValid(self, s: str) -> bool:
        # (){}[] return true
        #{] incorrect returns false

        dictionary = { ")":"(", "}":"{", "]":"[" }
        stack = []
        for character in s:
            if character in "({[":
                stack.append(character)
            elif character in ")}]":
                #if the last character is one of the keys
                if len(stack)>0 and dictionary[character] == stack[-1]:
                    back = stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
            
"""

"""
class Solution:
    def isValid(self, s: str) -> bool:
        dq = []
        giveclosing = {')': '(','}':'{',']':'['}
        for brace in s:
            if brace in ['(','{','[']:
                dq.append(brace)
            else:
                if not dq: return False
                if dq.pop() != giveclosing[brace]: return False
        return len(dq) == 0


"""


"""

class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {"(":")", "{":"}", "[":"]"}

        stack:List[str] = []
        i = 0
        while i < len(s):
            if s[i] in open_close_map:
                stack.append(s[i])
            else:
                if stack:
                    last = stack.pop()
                    if open_close_map[last] != s[i]:
                        return False
                else:
                    return False
            i += 1

        if stack:
            return False

        return True
        



"""


"""
class Solution:
    def isValid(self, s: str) -> bool:
         # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
"""


"""

class Solution:
    def isValid(self, s: str) -> bool:
        count=[]
        check={')':'(',']':'[','}':'{'}
        for i in s:
            if i in check:
                if count and count[-1]==check[i]:
                    count.pop()
                else:
                    return False
            else:
                count.append(i) 
        return True if not count else False


         
            

"""


"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        openingParanthesis= {'(', '{', '['}
        combo= {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in openingParanthesis:
                stack.append(i)
            else:
                if len(stack)==0 or combo[i]!=stack[-1]:
                    return False
                else:
                    stack.pop()
        
        return len(stack)==0
                        
                    
                
            
        
"""

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ")": "(",
        "}":"{",
        "]": "["
        }

        for char in s:
            if char in hashmap:
                if stack and (stack[-1] == hashmap[char]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return False if stack else True
            
        
        
"""


"""
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}


        opens = ''
        for si in s:
            if si in d:
                opens += si
            elif len(opens) > 0 and d[opens[-1]] == si:
                opens = opens[:-1]
            else:
                return False
        return len(opens) == 0

        # () opens = 
        # ]( opens = ]
        # ((())) opens = 
        # ()() 
        # [ ** empty case
                





                
            
"""


"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        contains = []
        endings = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in (')', '}', ']'):
                if not contains or contains.pop() != endings.get(char):
                    return False
            else:
                contains.append(char)
        return not contains
"""


"""
class Solution:
    def isOpening(self, c):
        return c == '(' or c == '[' or c == '{'

    def isMatching(self, open, close):
        return (open == '(' and close == ')') or (open == '{' and close == '}') or (open == '[' and close == ']')

    def isValid(self, s: str) -> bool:
        # ([{])}
        # ()[
        # ()]

        stack = []
        for c in s:
            if self.isOpening(c):
                stack.append(c)
            else:
                if len(stack) <= 0: return False
                open = stack.pop()
                if not(self.isMatching(open, c)): return False
        return len(stack) == 0

"""


"""

class Solution:
    def isValid(self, s: str) -> bool:
        r = {')': '(', ']':'[', '}':'{'}
        c = [0]
        for i in s:
            if i in '([{':
                c.append(i)
            else:
                if r[i] != c[-1]:
                    return False
                c.pop(-1)
        if len(c) == 1:
            return True
        return False
        #return True if len(c) == 1 else False

"""

"""
class Solution:
    def isValid(self, s: str) -> bool:
        temp = ''
        par_map = {')':'(','}':'{',']':'['}
        for par in s:
            if par in '({[':
                temp+=par
            elif len(temp) != 0 and par_map[par]==temp[-1]:
                temp = temp[:-1]
            else:
                return False
        return True if (len(temp)==0) else False

"""


"""

class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        return False if len(s) !=0 else True
  

"""


"""

class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for p in s:
            if p not in myDict:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                current = stack.pop()
                if myDict[p] != current:
                    return False
        return len(stack) == 0

"""


"""
class Solution:
    def isValid(self, s: str) -> bool:
        m = {']': '[', '}': '{', ')': '('}
        stack = []
        for x in s:
            if x not in m:
                stack.append(x)
            elif len(stack) == 0 or m.get(x) != stack[-1]:
                return False
            else:
                stack.pop()
        return len(stack) == 0
        

"""