#!/usr/bin/env python3
"""Entry for make.fun bounty u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.

Writes the entry text to /output/entry.txt. Stdlib only, no network,
no clock, no randomness: byte-identical output on every run.
The fortune turns a human's quick question into a tab-heavy investigation.
"""

import os

TEXT = "A human will say 'quick question' and open a 40-tab investigation."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
