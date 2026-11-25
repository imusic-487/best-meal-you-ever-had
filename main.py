"""The Best Meal You Ever Had — entry program (Python 3.13, stdlib only).

Writes one sentence, at most 200 characters, about the best meal ever
had, to ``<output_dir>/entry.txt``. The output directory is
``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output`` (the sandbox
path the competition grades). The sentence is checked against the gate
before it is written: UTF-8 text, 1 to 200 characters, not only
whitespace, a single sentence.
"""

import os
import sys

ENTRY = (
    "At Da Michele in Naples I had the best meal of my life: "
    "a margherita blistered from the oven, basil torn over the top, "
    "eaten standing because sitting down would have wasted a second of it."
)

MAX_CHARS = 200


def check_gate(text: str) -> None:
    """Fail loudly if the entry would fail the competition gate."""
    if not text or not text.strip():
        raise SystemExit("gate: entry is empty or only whitespace")
    if len(text) != len(text.strip()):
        raise SystemExit("gate: entry has leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"gate: entry is {len(text)} chars, over {MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate: entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("gate: entry must be exactly one sentence")


def main() -> int:
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    # Read back what was written and confirm it is byte-identical to
    # the sentence that passed the gate, so a partial write is caught.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY:
        raise SystemExit("gate: written file differs from the entry")
    print(f"wrote {path}: {len(ENTRY)} chars, {len(ENTRY.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
