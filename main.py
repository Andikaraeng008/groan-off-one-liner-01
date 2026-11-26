#!/usr/bin/env python3
"""The One-Liner Groan-Off entry: write one original one-line dad joke.

One concrete scene (dad buries the TV remote in the garden) with the
absurd twist in the final phrase: the tomatoes get to watch the family
argue about what to watch. Line length: 104 characters.
"""

import os

LINE = "Dad buried the TV remote in the garden so the tomatoes could finally watch us argue about what to watch."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
