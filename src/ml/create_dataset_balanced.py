import os
import pandas as pd
import random

safe = []
vulnerable = []

ROOT = "data/juliet/testcases"

for root, dirs, files in os.walk(ROOT):

    for file in files:

        if not (
            file.endswith(".c")
            or
            file.endswith(".cpp")
        ):
            continue

        path = os.path.join(root, file)

        try:

            with open(
                path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                code = f.read()

            if "bad" in file.lower():
                vulnerable.append(code)
            else:
                safe.append(code)

        except:
            pass

print("Safe:", len(safe))
print("Vulnerable:", len(vulnerable))

# Balancear
safe = random.sample(
    safe,
    min(len(safe), len(vulnerable))
)

rows = []

for x in safe:
    rows.append([x, 0])

for x in vulnerable:
    rows.append([x, 1])

df = pd.DataFrame(
    rows,
    columns=[
        "code",
        "label"
    ]
)

print(df["label"].value_counts())

df.to_csv(
    "data/juliet_balanced.csv",
    index=False
)

print("Dataset balanceado creado.")