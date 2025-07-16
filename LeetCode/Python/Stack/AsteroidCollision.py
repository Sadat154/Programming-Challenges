def asteroidCollision(asteroids):
    LEFT = 0
    RIGHT = 1

    if not asteroids:
        return []

    stack = []
    index = 0

    while index < len(asteroids):
        toCompare = asteroids[index]
        directiontoCompare = LEFT if toCompare < 0 else RIGHT

        # If stack is empty, just push
        if not stack:
            stack.append(toCompare)
            index += 1
            continue

        toCheck = stack[-1]
        directiontoCheck = LEFT if toCheck < 0 else RIGHT

        if directiontoCheck == RIGHT and directiontoCompare == LEFT:
            if abs(toCheck) > abs(toCompare):
                # toCheck survives, discard toCompare
                index += 1
            elif abs(toCheck) < abs(toCompare):
                # toCompare survives, remove toCheck, re-check with new top
                stack.pop()
            else:
                # Equal — both destroyed
                stack.pop()
                index += 1
        else:
            # No collision — just push
            stack.append(toCompare)
            index += 1

    return stack

print(asteroidCollision([2,4,-4,-1]))