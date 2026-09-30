def matrix_data():

    dependencies = ["pandas", "numpy", "matplotlib"]
    need_to_install = False
    for lib in dependencies:
        try:
            __import__(lib)
        except ImportError:
            print(f"[WARNING] {lib} is not installed.")
            need_to_install = True
    if need_to_install:
        print("\nTo install the missing dependencies, use pip or poetry:")
        print(" With pip:")
        print("  pip install -r requirements.txt")
        print("  python3 loading.py")
        print(" With Poetry:")
        print("  poetry install")
        print("  poetry run python loading.py")
    else:
        import pandas as pd
        import numpy as np
        import matplotlib as mpl
        print("LOADING STATUS: Loading programs...\n")
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
        print(f"[OK] matplotlib ({mpl.__version__}) - Visualization ready")
        import matplotlib.pyplot as mpl

        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        print("Generating visualization...\n")

        rng = np.random.default_rng()

        matrix_data = rng.normal(loc=50, scale=10, size=(50, 2))

        df = pd.DataFrame(matrix_data, columns=["Yellow Lanyard",
                                                "Orange Lanyard"])

        mpl.plot(df["Yellow Lanyard"], label="Yellow Lanyard")
        mpl.plot(df["Orange Lanyard"], label="Orange Lanyard")

        mpl.title("Matrix Data Analysis")
        mpl.xlabel("Project")
        mpl.ylabel("Grade")
        mpl.legend()
        print("Analysis complete!")
        mpl.savefig("matrix_analysis.png")
        print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    matrix_data()
