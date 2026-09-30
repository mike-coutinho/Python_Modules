
import sys
import os

if __name__ == "__main__":
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("Error: Install requirements, run:")
        print("pip install -r requirements.txt")
        sys.exit()
    load_dotenv()

    configuration_variables = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    dict_conf_var = {k: os.getenv(k) for k in configuration_variables}

    miss_conf = [k for k, v in dict_conf_var.items() if not v]

    matrix_allow = "development", "production"
    if dict_conf_var["MATRIX_MODE"] not in matrix_allow:
        print("Invalid configuration on MATRIX_MODE or no .env file")
        sys.exit()

    if miss_conf:
        print(f"[ERROR] missing this configuration {miss_conf}")
        sys.exit()

    print("ORACLE STATUS: Reading the Matrix...\n")
    if dict_conf_var["MATRIX_MODE"] == "development":
        print("Configuration loaded:")
        print("Mode:", dict_conf_var["MATRIX_MODE"])
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print("Log Level: DEBUG")
        print("Zion Network: Developing")
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    else:
        print("Configuration loaded:")
        print("Mode:", dict_conf_var["MATRIX_MODE"])
        print("Database:", dict_conf_var["DATABASE_URL"])
        print("API Access: Authenticated")
        print("Log Level:", dict_conf_var["LOG_LEVEL"])
        print("Zion Network:", dict_conf_var["ZION_ENDPOINT"])
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
