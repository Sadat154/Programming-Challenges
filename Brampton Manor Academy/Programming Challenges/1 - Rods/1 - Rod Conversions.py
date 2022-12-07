

def rTm(rods):
    rodsToMeters = rods * 5.0292
    return rodsToMeters


def rTf(rodsToMeters):
    rodsToFeet = rodsToMeters / 0.3048
    return rodsToFeet

def rTmi(rodsToMeters):
    rodsToMiles = rodsToMeters / 1609.34
    return rodsToMiles

def rTfu(rods):
    rodsToFurlongs = rods / 40
    return rodsToFurlongs

def minutes(rodsToMiles):
    rodMinutes = (rodsToMiles / 3.1) * 60
    return rodMinutes


def run():
    rods = float(input("Input Rods: "))
    print(f"Meters: {rTm(rods)}")
    print(f"Feet: {rTf(rTm(rods))}")
    print(f"Miles: {rTmi(rTm(rods))}")
    print(f"Furlongs: {rTfu(rods)}")
    print(f"Minutes to walk {rods}: {minutes(rTmi(rTm(rods)))}")

if __name__ == "__main__":
    run()
    
    
   ####################
def pascals(p):
    result = [[1],[1,3,3,1]]

    middle_num = [sum(result[-1][x:x + 2]) for x in range(len(result[-1]) - 1)]
    answer = [x for x in middle_num]
    print(answer)







print(pascals(5))
    
    
    
    #####################
   

def fibonacci_series(n):
    answer = [1,2]
    for i in range(n-2):
        answer.append(sum(answer[i:i+2]))

    return answer[::-1]

def zeckendorf_representation(n, fibonacci):
    resultList = []
    answer = n
    counter = 0

    test = [x for x in fibonacci if x < 53316291173]

    # Q1b answe = 832040 as thats the largest output answer when n = 1000000
    print(test[0:])
    for i in range(53316291173,0 , -1):
        arr = []
        q = i

        for j in test:
            if q - j >= 0:
                q -= j
                arr.append(j)
            if len(arr) > 3:
                break
        if len(arr) == 3:
            counter += 1

    return counter



    # for i in fibonacci:
    #     if answer - i >= 0:
    #         answer -= i
    #         resultList.append(i)
    # return resultList





if __name__ == '__main__':
    fibonacci = fibonacci_series(100000)
    userChoice = int(input("Please choose the number: "))
    print(zeckendorf_representation(userChoice,fibonacci))

    
    
    
    
            
