class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(0, len(s)):
            if ((s[i] == "[") or
             (s[i] == "(") or
            (s[i] == "{")):
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                bracket = stack.pop()

                if ((bracket == "(" and s[i] != ")") or
                 (bracket == "[" and s[i] != "]") or
                 (bracket == "{" and s[i] != "}")):
                    return False

        if len(stack) != 0:
            return False
        return True