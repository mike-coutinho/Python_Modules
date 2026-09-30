class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WateringError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def test_garden_errors() -> None:
    print("Testing catching all garden errors...")
    try:
        raise GardenError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}")


def test_plant_errors() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught {error.__class__.__name__}: {error}")


def test_watering_errors() -> None:
    print("Testing WaterError...")
    try:
        raise WateringError("Not enough water in the tank!")
    except WateringError as error:
        print(f"Caught {error.__class__.__name__}: {error}")


if __name__ == "__main__":
    print("=== Garden Custom Errors Demo ===")

    print()
    test_plant_errors()
    print()
    test_watering_errors()
    print()
    test_garden_errors()
    print()
    print("All custom error types work correctly!")
