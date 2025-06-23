def calPoints(operations):
    record = []

    for i in operations:
        if i.isnumeric() or i[1:].isnumeric():
            record.append(int(i))
        elif i == "+":
            record.append(record[-1] + record [-2])

        elif i == "C":
            record.pop()

        else:
            record.append(record[-1]*2)

    return sum(record)

print(calPoints(["1","2","+","C","5","D"]))