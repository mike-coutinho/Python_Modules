import sys
import os
import site


def virtual_environment_and_python_checks() -> None:
    if is_virtual_environment():
        print("\nMATRIX STATUS: Welcome to the construct\n")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")

    if is_virtual_environment():
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
    else:
        print("Virtual Environment: None detected\n")


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    virtual_environment_and_python_checks()

    if is_virtual_environment():
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the"
              "global system.\n")
        print("Package installation path:")
        print(site.getsitepackages()[0])
    else:
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
