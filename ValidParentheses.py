'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            #print(stack)
            if c == '(' or c == '{' or  c == '[':
                stack.append(c)
            elif c == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
            elif c == '}':
                if len(stack) != 0 and  stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
            elif c == ']':
                if len(stack) != 0 and  stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True
