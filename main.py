#!/usr/bin/env python3
"""Produce a single funny line for /output/entry.txt.

The joke turns on a familiar debugging reflex: when something works
immediately, a programmer trusts the success so little that the rest
of the day goes into hunting for the hidden damage. This program
builds that line out of three short pieces, checks the assembled
result against the contest limits, writes it out, and then reads the
file back to confirm the bytes on disk are exactly the bytes intended.
Only the Python standard library is used, and repeated runs always
produce identical output.
"""

import os

DESTINATION = "/output/entry.txt"
LIMIT = 200

# The line, split at its natural joints. The opening reports an
# unlikely clean success, the middle stretches that moment across a
# whole day, and the ending admits what the day was actually spent on.
OPENING = "My code worked on the first try"
MIDDLE = "so I spent the rest of the day"
ENDING = "looking for what I broke."


def assemble() -> str:
    """Join the three pieces into one sentence and validate it."""
    sentence = OPENING + ", " + MIDDLE + " " + ENDING
    if len(sentence) < 1 or len(sentence) > LIMIT:
        raise ValueError("length %d is outside 1..%d" % (len(sentence), LIMIT))
    if sentence.strip() == "":
        raise ValueError("a blank entry is not allowed")
    if sentence != sentence.strip():
        raise ValueError("surrounding whitespace is not allowed")
    if "\n" in sentence or "\r" in sentence or "\t" in sentence:
        raise ValueError("the entry must stay on one line")
    if "  " in sentence:
        raise ValueError("words must be separated by single spaces")
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("the entry must be exactly one sentence")
    if "?" in sentence or "!" in sentence:
        raise ValueError("the entry must be a plain statement, not a question or exclamation")
    if not OPENING.endswith("first try"):
        raise ValueError("the opening must end with the unlikely success")
    if "rest of the day" not in MIDDLE:
        raise ValueError("the middle must stretch the moment across the day")
    if not ENDING.startswith("looking for"):
        raise ValueError("the ending must admit the search for damage")
    encoded = sentence.encode("utf-8")
    if len(encoded) != len(sentence):
        raise ValueError("the entry is expected to be plain ASCII text")
    return sentence


def run() -> None:
    sentence = assemble()
    folder = os.path.dirname(DESTINATION)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as stream:
        stream.write(sentence)
    with open(DESTINATION, "rb") as stream:
        on_disk = stream.read()
    if on_disk != sentence.encode("utf-8"):
        raise ValueError("the file on disk differs from the assembled line")


if __name__ == "__main__":
    run()
