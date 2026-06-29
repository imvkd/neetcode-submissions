class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for n in s:
            if n not in map:
                stack.append(n)
            else:
                if stack and map[n] == stack[-1]:
                    stack.pop()
                    # print(stack)
                else:
                    return False

        return len(stack) == 0