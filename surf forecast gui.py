print("wind and swell gui")

# Get offshore input
isOffshore = input("Is it blowing offshore? (true/false): ").strip().lower()
if isOffshore in ['true', 't', 'yes', 'y']:
    isOffshore = True
elif isOffshore in ['false', 'f', 'no', 'n']:
    isOffshore = False
else:
    raise ValueError("Invalid input: Please enter 'true' or 'false'.")

# Get onshore input
isOnshore = input("Is it blowing onshore? (true/false): ").strip().lower()
if isOnshore in ['true', 't', 'yes', 'y']:
    isOnshore = True
elif isOnshore in ['false', 'f', 'no', 'n']:
    isOnshore = False
else:
    raise ValueError("Invalid input: Please enter 'true' or 'false'.")

# Get sideshore input
isSideshore = input("Is it blowing sideshore? (true/false): ").strip().lower()
if isSideshore in ['true', 't', 'yes', 'y']:
    isSideshore = True
elif isSideshore in ['false', 'f', 'no', 'n']:
    isSideshore = False
else:
    raise ValueError("Invalid input: Please enter 'true' or 'false'.")

# Get wind speed, swell period, and swell height
wind = float(input("Enter the wind in Kts: "))  
print(str(wind) + " Kts")

swell = float(input("Enter the swell second period: "))  
print(str(swell) + " s")

swellHeight = float(input("Enter the wave height in feet: "))  
print(str(swellHeight) + " Ft")


if isOffshore and wind <= 9 and swell >= 8 and swellHeight >= 4:
    print("IT IS FIRING")
elif isOffshore and wind > 9 and swell > 8 and swellHeight > 4:
    print("expect the wind to push you back try to take off closest to the peak")
elif isOffshore and wind >= 15:
    print("Dont bother")
elif isOffshore and wind < 9 and swell < 15 and swellHeight > 3:
    print("Florida sandbars arent the strongest anywhere else in the world it would be GOOD here it will close out")
elif isOffshore and swellHeight <= 2:
    print("its a glassy lake.")
else:
    print("not configured")