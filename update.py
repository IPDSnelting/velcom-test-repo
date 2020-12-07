#!/usr/bin/env python

import json
import math
import random
import subprocess

def main():
    commit_count = subprocess.run(
        ["git", "rev-list", "--count", "HEAD"],
        capture_output=True,
        text=True,
    )
    commit_count = int(commit_count.stdout.strip())

    x = commit_count / 10

    sigma1 = math.sin(x)/10 + 0.5 # Between 0.4 and 0.6
    mu1 = math.cos(x/5) * 10 + 100 # Between 90 and 110
    values1 = [random.gauss(mu1, sigma1) for i in range(40)]

    sigma2 = (math.cos(x/7) + 1) / 200 # Between 0 and 0.01
    mu2 = math.sin(x/2)/3 + (1/6) # Between 1/6 and 5/6
    values2 = [random.gauss(mu2, sigma2) for i in range(50)]

    result = {
        "test": {
            "value1": {
                "unit": "furlong",
                "interpretation": "MORE_IS_BETTER",
                "values": values1,
            },
            "value2": {
                "unit": "badingles",
                "interpretation": "NEUTRAL",
                "values": values2,
            },
        },
    }

    with open("bench-result.json", "w") as f:
        json.dump(result, f, indent=4)
        f.write("\n")

    subprocess.run(["git", "add", "bench-result.json"])
    subprocess.run(["git", "commit", "-m", f"Update {commit_count}"])

if __name__ == "__main__":
    main()
