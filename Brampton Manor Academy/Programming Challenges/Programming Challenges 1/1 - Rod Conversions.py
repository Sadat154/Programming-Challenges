


def rods_to_meters(rods):
    rodsToMeters = rods * 5.0292
    return rodsToMeters


def rods_to_feet(rodsToMeters):
    rodsToFeet = rodsToMeters / 0.3048
    return rodsToFeet


def rods_to_miles(rodsToMeters):
    rodsToMiles = rodsToMeters / 1609.34
    return rodsToMiles


def rods_to_furlongs(rods):
    rodsToFurlongs = rods / 40
    return rodsToFurlongs


def minutes_calculation(rodsToMiles):
    rodMinutes = (rodsToMiles / 3.1) * 60
    return rodMinutes


# print("Meters:",rTm(rods),"Feet:", rTf(rTm(rods)), "Miles:",rTmi(rTm(rods)),"Furlongs:", rTfu(rods),"Minutes To walk", rods, "rods:", minutes(rTmi(rTm(rods))))
def run():
	rods = float(input("Input Rods: "))
	print(f"Meters: {rods_to_meters(rods)}")
	print(f"Feet: {rods_to_feet(rods_to_meters(rods))}")
	print(f"Miles: {rods_to_miles(rods_to_meters(rods))}")
	print(f"Furlongs: {rods_to_furlongs(rods)}")
	print(f"Minutes to walk {rods}: {minutes_calculation(rods_to_miles(rods_to_meters(rods)))}")


if __name__ == "__main__":
    run()
