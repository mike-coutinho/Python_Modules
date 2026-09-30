import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Acessing file '{sys.argv[1]}'")
    try:
        file = open(sys.argv[1])
        print("---\n")
        file_content = file.read()
        print(f"{file_content}\n")
        file.close()
        print(f"File '{sys.argv[1]}' closed.\n")
        print("Transform data:")
        print("---\n")
        file_content = "\n".join(
            line + "#" for line in file_content.splitlines()
            )
        print(f"{file_content}\n")
        print("---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        user_input = sys.stdin.readline().strip()

        if user_input:
            new_file = open(user_input, "w")
            print(f"Saving data to '{user_input}'.")
            new_file.write(file_content)
            new_file.close()
            print(f"Data saved in file '{user_input}'.")
        else:
            print("Not saving data.")
    except Exception as error:
        sys.stderr.write(
            f"[STDERR] Error opening file '{sys.argv[1]}': {error}\n"
            )
