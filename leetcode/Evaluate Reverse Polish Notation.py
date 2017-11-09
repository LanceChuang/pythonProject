# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # corner case: if input is 0 or None
        if not tokens or tokens == 0:
            return 0
        
        stack = []
        for i in tokens:
            if i == "+":
                element1 = stack.pop()
                element2 = stack.pop()
                newOne = element1 + element2
                stack.append(newOne)
            elif i == "-":
                element1 = stack.pop()
                element2 = stack.pop()
                newOne = element2 - element1
                stack.append(newOne)
            elif i == "*":
                element1 = stack.pop()
                element2 = stack.pop()
                newOne = element1 * element2
                stack.append(newOne)
            elif i == "/": # 會有負數情況要處理 : if 1/-22 => return 0 but in python it return -1
                element1 = stack.pop()
                element2 = stack.pop()
                if element1 * element2 < 0 and element2 % element1 != 0:
                    stack.append(element2 / element1 + 1)
                else:
                    stack.append(element2 / element1)
            else:
                stack.append(int(i))
        
        return stack.pop()
                
                
        