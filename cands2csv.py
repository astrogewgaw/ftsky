import argparse
import pandas as pd
from your import Your
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="cands2csv.py",
        description="Convert TransientX output to Your-style CSV file.",
    )
    parser.add_argument("txt", help="Text file to convert.", required=True)
    args = parser.parse_args()

    hdr = Your(fil).your_header
    txt = Path(args.filename).absolute()
    cands = pd.read_csv(
        txt,
        sep="\t",
        names=[
            "beam",
            "id",
            "stime",
            "dm",
            "width",
            "snr",
            "fh",
            "fl",
            "png",
            "ddplanid",
            "file",
        ],
    ).sort_values(by="stime")
    cands = (
        cands.sort_values(by="stime")
        .drop(columns=["beam", "id", "fh", "fl", "png", "ddplanid", "file"])
        .assign(
            stime=cands["stime"].values - hdr.tstart,
            width=cands["width"].values / hdr.tsamp,
        )
    )
    cands["num_files"] = 1
    cands.insert(5, "label", 0)
    cands.insert(0, "file", fil)
    cands["chan_mask_path"] = pd.NA
    cands.to_csv("candidates.csv", index=False)
