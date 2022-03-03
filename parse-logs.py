import sys
import pandas as pd

columns = ["Set", "Swaps", "Tree height", "Init (s)", "Param gen (s)", "Synthesis (s)",
           "Prover (s)", "Verifier (s)", "Hash function"]

# filename = "merkle-snarks-baseline.log"


def parse_logs(filename):
    data = []
    file = open(filename, 'r')
    for line in file:
        if line.startswith("merkle,"):
            data.append(line)

    df = pd.DataFrame([x.rstrip().split(",") for x in data], columns=columns)

    gb = df.groupby("Hash function")
    for x in gb.groups:
        df_t = gb.get_group(x)
        savefile = "{}-{}-single.csv".format(
            df_t["Hash function"].iloc[0].lower(), df_t["Tree height"].iloc[0])
        del df_t["Hash function"]
        df_t.to_csv(savefile, header=None, index=False)

    del df["Set"]
    df[df.columns[0]] = df[df.columns[0]].astype(int)
    df[df.columns[1]] = df[df.columns[1]].astype(int)
    for col in df.columns[2:-1]:
        df[col] = df[col].astype(float)
    df = df.rename(columns={"Tree height": "# Merkle Proofs"})
    df["# Merkle Proofs"] = 2 * df["Swaps"]
    del df["Swaps"]

    gb = df.groupby("Hash function")
    for x in gb.groups:
        print(gb.get_group(x).to_string(index=False))


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        parse_logs(filename)
    except:
        raise
