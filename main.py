#!/usr/bin/env python3
"""The One-Liner Groan-Off entry: write one original one-line dad joke.

One concrete scene (dad at a family barbecue) with the wordplay twist
in the final phrase: "grilling synonyms".
"""

import os

LINE = "My dad replaced our doorbell with a knock-knock joke, so now every visitor has to finish the punchline before we open the door."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
