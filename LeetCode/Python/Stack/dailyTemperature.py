def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()

            result[stackInd] = i - stackInd
        stack.append((t, i))
    return result




print(dailyTemperatures([30,38,30,36,35,40,28]))

