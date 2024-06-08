class Solution:
    def decodeString(self, s: str) -> str:
        def helper(string, loop):
            ret_string = ''
            for l in range(loop):
                num = ''
                inner = ''
                stack = []

                for c in string:
                    if c.isdigit() and len(stack) == 0:
                        num += c
                    elif c == '[':
                        stack.append('[')
                        if len(stack) == 1:
                            continue
                        inner += c
                    elif c == ']':
                        stack.pop()
                        if len(stack) == 0:
                            ret_string += helper(inner, int(num))
                            inner, num = '', ''
                            continue
                        inner += c
                    elif len(stack) > 0:
                        inner += c
                    else:
                        ret_string += c
            return ret_string

        ans = helper(s, 1)
        return ans
                    