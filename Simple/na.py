# 20. Valid Parenthesis
## deque(), double-linked list, O(1) pop() and append()           
## List can do pop() append() too, but O(n)
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        dict_brkt = {')':'(',']':'[','}':'{'}
        stack = deque()
        for i in s: # only 
            if i in dict_brkt:
                if not stack or stack.pop() != dict_brkt[i]:
                    return False
            else:
                stack.append(i)
        return not stack
