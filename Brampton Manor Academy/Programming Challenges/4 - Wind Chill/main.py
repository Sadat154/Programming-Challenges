temperatureList = [10.0,0.0,-10.0]
windSpeedList = [15,25,35]


def calculateWindChill(air_speed,air_temp):
    windChill = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return windChill

def run():
    for i in range (len(temperatureList)):
        print(f"Temperature of {temperatureList[i]} and speed of {windSpeedList[i]} gives windchill of: {calculateWindChill(windSpeedList[i],temperatureList[i])}")
    temperature = float(input("Temperature: "))
    speed = float(input("Speed: "))
    windchill = calculateWindChill(speed,temperature)
    print(f"Windchill: {windchill}")


if __name__ == "__main__":
    run()