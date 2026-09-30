def secure_archive(
        filename: str, option: str, to_write: str) -> tuple[bool, str]:
    try:
        with open(filename, option) as file:
            if option == "r":
                return True, file.read()
            else:
                file.write(to_write)
                return True, "Content successfully written to file"
    except Exception as error:
        return False, str(error)


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")

    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r", "teste"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("secure_archive", "r", "teste"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("ancient_fragment.txt", "r", "teste"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("test.txt", "w", "teste"))
