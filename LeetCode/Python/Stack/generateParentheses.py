from fileinput import close


def is_valid(s):
    balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def generate_parentheses_brute(n):
    result = []
    stack = [("", 0, 0)] # currentstr, openbrack, closedbrak

    while stack:
        current, open_c, close_c = stack.pop()

        if len(current) == 2*n:
            result.append(current)

        if open_c < n:
            stack.append((current+ "(", open_c +1, close_c))

        if close_c < open_c:
            stack.append((current+")", open_c, close_c+1))
        print(stack)
    print(result)



print(generate_parentheses_brute(3))
