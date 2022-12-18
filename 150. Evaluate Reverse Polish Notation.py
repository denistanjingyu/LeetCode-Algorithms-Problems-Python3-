class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                first_int = stack.pop()
                second_int = stack.pop()
                stack.append(second_int - first_int)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                first_int = stack.pop()
                second_int = stack.pop()
                result = 0
                if second_int / first_int < 0:
                    result = ceil(second_int / first_int)
                elif second_int / first_int > 0:
                    result = floor(second_int / first_int)
                stack.append(result)
            else:
                stack.append(int(char))
        
        return stack[-1]