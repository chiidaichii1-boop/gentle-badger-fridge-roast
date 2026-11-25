#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast of a smart fridge (at most 200 characters) to
``<output_dir>/entry.txt``.

The roast targets the ice maker, one of the most fridge-specific parts of
a smart fridge, and dodges the obvious cracks about ordering groceries or
watching the owner: instead of a camera or a shopping list, the joke is
that the ice maker behaves like a resentful employee with exactly two
moods -- a full avalanche, or a single cube handed over grudgingly.
"""

import os

# The entry: one line, well under the 200-character cap, no trailing
# newline (the gate counts characters, so the file holds exactly this).
ENTRY = (
    "My smart fridge's ice maker has two settings: avalanche, "
    "and one single cube it clearly resents making."
)


def main() -> None:
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _ = input_dir  # This entry needs no input data; the roast is fixed.

    # Never delete the output folder: create it if missing and write
    # inside it.
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
