#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from 1800, using only words and things a
person from that year could already picture: a road, a post office, a
library, a letter, a book. No word coined after 1800 appears.

Usage:
    python3 main.py [--output /output/entry.txt]
"""

import argparse
import os
import re
import sys

# Words coined after 1800 that must never appear in the entry.
FORBIDDEN = {
    "computer", "screen", "website", "email", "phone", "telephone",
    "internet", "electricity", "electric", "digital", "online", "web",
    "software", "keyboard", "television", "radio", "wireless",
}


def validate(sentence: str) -> None:
    """Fail loudly if the sentence breaks the bounty gate."""
    if not (1 <= len(sentence) <= 200):
        sys.exit(f"entry is {len(sentence)} characters, must be 1-200")
    if sentence != sentence.strip() or not sentence.strip():
        sys.exit("entry must not be only white space")
    if sentence.count(".") != 1 or not sentence.endswith("."):
        sys.exit("entry must be exactly one sentence")
    words = set(re.findall(r"[a-z]+", sentence.lower()))
    bad = words & FORBIDDEN
    if bad:
        sys.exit(f"post-1800 words in entry: {sorted(bad)}")


SENTENCE = (
    "Picture every library and post office on earth joined by a single "
    "road of light, so any letter or book can reach any door in the "
    "blink of an eye."
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write the one-sentence entry to a text file."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="Path of the file to write (default: /output/entry.txt).",
    )
    args = parser.parse_args()

    validate(SENTENCE)

    parent = os.path.dirname(os.path.abspath(args.output))
    os.makedirs(parent, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(SENTENCE)

    print(f"wrote {len(SENTENCE)} characters to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
