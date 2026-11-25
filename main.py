#!/usr/bin/env python3
"""make.fun -- "Make the AI Judge Laugh".

Writes one joke about office life, a single line under 200 characters,
to /output/entry.txt.

Deterministic: the text is a constant. No randomness, no clock,
no network, standard library only.
"""

import os
import sys

TEXT = "Our sprint review is twelve people taking turns saying 'basically done' about work nobody started."

# The gate requires 1-200 characters of UTF-8 text, not only whitespace.
if not 1 <= len(TEXT) <= 200 or not TEXT.strip():
    raise SystemExit(f"TEXT must be 1-200 characters, got {len(TEXT)}")
if "\n" in TEXT:
    raise SystemExit("TEXT must be a single line")


def main() -> None:
    if len(sys.argv) > 1:
        out = sys.argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        out = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revisi: output sudah dicek ulang dan tetap stabil di setiap run.
