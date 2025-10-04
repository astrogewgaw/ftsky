#!/usr/bin/env python

import argparse
import numpy as np
import pandas as pd
from your import Your
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="cands2csv.py",
        description="Convert TransientX output to Your-style CSV file.",
    )
    parser.add_argument("txt", help="TransientX output")
    parser.add_argument("-f", "--fil", help="Filterbank file", required=True)
    args = parser.parse_args()
    fil = str(Path(args.fil).absolute())
    txt = str(Path(args.txt).absolute())

    hdr = Your(fil).your_header
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
            stime=(cands["stime"].to_numpy() - hdr.tstart) * 24 * 60 * 60,
            width=(cands["width"].to_numpy() * 1e-3 / hdr.tsamp).astype(int),
        )
    )
    cands["num_files"] = 1
    cands.insert(5, "label", 0)
    cands["chan_mask_path"] = pd.NA
    cands.insert(0, "file", Path(fil).name)
    cands.to_csv("candidates.csv", index=False)
