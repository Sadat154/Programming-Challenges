

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