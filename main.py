"""Five Seconds to Explain the Glass — make.fun entry.

Writes one sentence (<=200 chars) to /output/entry.txt: the excuse a
house cat gives in the five seconds after knocking a glass off the table,
in the cat's own voice. No apology, no confession — just the most
convincing case a cat can make for itself.
"""

import os
import sys

ENTRY = (
    "The glass was sitting in my sunbeam, and I am legally the "
    "sunbeam's owner, so the glass was trespassing and I evicted it."
)

MAX_CHARS = 200


def check_entry(text):
    """Validate one sentence, 1..200 chars, no leading/trailing space."""
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters: %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: a single terminal period, nothing after it.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def write_entry(out_dir, text):
    """Write the validated entry to <out_dir>/entry.txt."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    text = check_entry(ENTRY)
    path = write_entry(out_dir, text)
    print("wrote %s (%d chars)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
