def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        print("Testing operation 0...")
        int("abc")
    elif operation_number == 1:
        print("Testing operation 1...")
        10 / 0
    elif operation_number == 2:
        print("Testing operation 2...")
        open("/non/existent/file", "r")
    elif operation_number == 3:
        print("Testing operation 3...")
        "string" + 5


def test_error_types() -> None:
    for i in range(4):
        try:
            garden_operations(i)
        except Exception as error:
            print(f"Caught {error.__class__.__name__}: {error}")
    print("Testing operation 4...")
    print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
