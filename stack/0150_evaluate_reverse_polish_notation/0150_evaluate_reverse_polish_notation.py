
import operator

class Solution(object):
    def evalRPN(self, tokens):
        numerals = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.div
            }

        for token in tokens:
            if token not in operators:
                numerals.append(int(token))
            else:
                y, x = numerals.pop(), numerals.pop()
                numerals.append(int(operators[token](x * 1.0, y)))
        return numerals.pop()


tokens = ["2","1","+","3","*"]
res = Solution().evalRPN(tokens)
print(res)