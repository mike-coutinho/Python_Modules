import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Acessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1])
            print("---\n")
            print(f"{file.read()}\n")
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
        except Exception as error:
            print(f"Error opening file '{sys.argv[1]}': {error}")
