class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() == plant_name:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
    except Exception as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    try:
        water_plant("Lettuce")
    except Exception as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    try:
        water_plant("Carrots")
    except Exception as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    finally:
        print("Closing watering system")

    print()

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
    except Exception as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    try:
        water_plant("lettuce")
    except Exception as error:
        print(f"Caught {error.__class__.__name__}: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")
