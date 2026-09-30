def input_temperature(temp_str: str) -> int | None:
    print()
    print(f"Input data is '{temp_str}'")
    try:
        test = int(temp_str)
        if test < 0:
            raise Exception(f"{temp_str}°C is too cold for plants (min 0°C)")
        elif test > 40:
            raise Exception(f"{temp_str}°C is too hot for plants (max 40°C)")
        print(f"Temperature is now {temp_str}°C.")
        return test
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
        return None


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("abc")
    input_temperature("100")
    input_temperature("-50")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
