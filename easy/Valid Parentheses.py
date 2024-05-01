# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = {'(': ')',
                         '{': '}',
                         '[': ']'
                        }
        stack = []
        for bracket in s:
            if bracket in brackets_dict.keys():
                stack.append(bracket)
            else:
                if not stack or brackets_dict[stack.pop()]!=bracket:
                    return False
        return True if not stack else False