def getSum(a, b):
    carry = 0
    res = 0
    test = ""

    for i in range(32):

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)


print(getSum(6,8))
