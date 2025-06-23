def evalRPN(expression):
    stack = []
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)  # Truncates toward zero
    }

    for i in expression:
        if i.lstrip('-').isdigit():  # Handles negative numbers too
            stack.append(int(i))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(ops[i](num1, num2))
    return stack.pop()
