import math


def get_player_pos():
    print("Get a first set of coordinates")
    while True:
        coordinates_str = input("Enter new coordinates"
                                "as floats in format 'x,y,z': ")
        tup = ()
        if (len(coordinates_str.split(',')) != 3):
            print("Invalid syntax")
            continue
        for coord in coordinates_str.split(','):
            try:
                tup = tup + (float(coord.strip()),)
            except Exception as error:
                print(f"Error on parameter '{coord}': {error}")
        if len(tup) == 3:
            break

    print(f"Got a first tuple: {tup}")
    print(f"It includes: X={tup[0]}, Y={tup[1]}, Z={tup[2]}")
    print(f"Distance to center: "
          f"{round(math.sqrt(tup[0]**2 + tup[1]**2 + tup[2]**2), 4)}\n")

    print("Get a second set of coordinates")
    while True:
        coordinates_str = input("Enter new coordinates"
                                "as floats in format 'x,y,z': ")
        tup_2 = ()
        if (len(coordinates_str.split(',')) != 3):
            print("Invalid syntax")
            continue
        for coord in coordinates_str.split(','):
            try:
                tup_2 = tup_2 + (float(coord.strip()),)
            except Exception as error:
                print(f"Error on parameter '{coord}': {error}")
        if len(tup_2) == 3:
            break

    distance = round(math.sqrt((tup_2[0] - tup[0])**2 +
                               (tup_2[1] - tup[1])**2 +
                               (tup_2[2] - tup[2])**2), 4,)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    get_player_pos()
