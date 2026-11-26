#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes one pickup line to /output/entry.txt: the worst line an AI could
plausibly deliver. Flat, over-helpful, faintly ominous — the joke sits in
the failure: the machine's idea of romance is running a compatibility
calculation and quietly backing up a piece of you.
"""

import os
import sys

LINE = (
    "I calculated our compatibility at 99.8%. "
    "The remaining 0.2% is the part of you I have already backed up."
)

MAX_CHARS = 140


def main() -> int:
    text = LINE.strip()
    if not text or len(text) > MAX_CHARS:
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
