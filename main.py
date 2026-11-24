#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one single-line review of planet Earth, left by an alien
tourist, to /output/entry.txt (UTF-8, 132 Unicode code points,
inside the 1-200 gate). Deterministic, standard library only,
no network, no input.

The line: the locals photograph their food before eating it, as
if it might escape -- an ordinary human habit seen from outside,
not traffic, gravity, money or weather. The alien waited along
with them, so its own meal went cold; the verdict still lands
positive, with a star rating, like a real tourist review. One
joke, one turn, punch at the end.
"""

import os

REVIEW = (
    "The locals photograph their food before eating it, "
    "as if it might escape. Mine went cold while I waited. "
    "Still delicious. 4/5 stars."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    # REVIEW is exactly 132 Unicode code points: inside the 1-200 gate.
    # Fail loudly instead of shipping an invalid entry if it ever changes.
    assert 1 <= len(REVIEW) <= 200, "review must be 1-200 characters"
    assert REVIEW.strip() == REVIEW, "review must not be only whitespace"
    assert "\n" not in REVIEW, "review must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(REVIEW)


if __name__ == "__main__":
    main()
