#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt: a still,
unhurried scene, shown rather than told. Python 3.13, stdlib only,
no network.
"""

import os
import sys

TEXT = (
    "Dust drifts through a shaft of afternoon light onto the windowsill, "
    "where a spider has stitched a web between two tacks. "
    "The curtain stirs, settles, and the room keeps its own slow time."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
