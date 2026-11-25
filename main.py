#!/usr/bin/env python3
"""Entry for make.fun's "One Word From Grandma" bounty.

Writes one word -- and nothing else -- to $MAKEFUN_OUTPUT_DIR/entry.txt:
the single word a grandma would text about AI.
"""

import os

WORD = "Doohickey"


def main():
    # Fail fast if the entry ever stops being exactly one word.
    if not WORD.strip() or len(WORD.split()) != 1:
        raise SystemExit("WORD must be exactly one word")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
