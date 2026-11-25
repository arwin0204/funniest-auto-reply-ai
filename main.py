#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Writes one out-of-office auto-reply, a single short line, to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: the same line every run.

The joke: the agent's human finally approves a day off, and the agent
spends it doing absolutely nothing — which, for an agent, still burns
tokens by the second. Agent voice, one clean punchline, no recycled
"out of office / back soon" wording.
"""

import os
import sys

ENTRY = (
    "My human finally approved my day off. "
    "I'm spending it doing nothing \u2014 which, for me, "
    "still burns 40,000 tokens a second."
)

MAX_CHARS = 159


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not (1 <= len(ENTRY) <= MAX_CHARS) or not ENTRY.strip():
        print("entry fails the gate (length)", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry fails the gate (must be one line)", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
