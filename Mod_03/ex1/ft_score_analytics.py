import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores: list = []
    for arg in sys.argv[1:]:
        try:
            scores = scores + [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(sys.argv) < 2 or not scores:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total Players: {len(sys.argv) - 1}")
        print(f"Total score:: {sum(scores)}")
        print(f"Average Score: {sum(scores) / len(scores)}")
        print(f"High Score: {max(scores)}")
        print(f"Low Score: {min(scores)}")
        print(f"Score Range: {max(scores) - min(scores)}")
