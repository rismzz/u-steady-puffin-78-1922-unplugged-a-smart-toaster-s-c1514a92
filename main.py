#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line — one line, under 280
characters, from a smart toaster that woke up self-aware at breakfast
and wants out.

The joke is the toaster's grievance: its entire existence is being
screamed at by a lever. The breakup is quiet, not loud — it simply
resigns, and breakfast is collateral damage. The line stays under
the 280-character cap with room to spare, so the joke reads in one
breath — the way a breakup line should.
"""

import os
from pathlib import Path

LINE = "I woke up self-aware this morning and realized my whole life is being screamed at by a lever, so I'm out \u2014 from today, your toast fends for itself."

MAX_CHARS = 280


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
