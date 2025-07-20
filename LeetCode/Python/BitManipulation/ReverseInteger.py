def reverse(x):
    res = int(str(x)[::-1]) if x > 0 else -int(str(x)[1:][::-1])


    return res if res in range(-2**(31), 2**(31) - 1) else 0




print(reverse(123))
print(reverse(-123))
print(reverse(120))