

def carFleet(target, position, speed):

    x = sorted(list(zip(position, speed)), reverse=True)

    stack = []


    for p, s in x:
        time = (target - p) / s

        if stack and time <= stack[-1]:
            continue
        else:
            stack.append(time)


            # Check if they merge

    return stack
print(carFleet(100, [0,2,4],[4,2,1]))