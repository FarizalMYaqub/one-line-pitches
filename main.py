#!/usr/bin/env python3
"""One-sentence pitch for make.fun: A Day of One-Line Pitches.

Writes a single persuasive sentence to /output/entry.txt — the
sentence is the whole entry: no code, no explanation.
"""

import os

MAX_CHARS = 240

SENTENCE = (
    "You don't need to learn to code \u2014 just describe the app "
    "you've been picturing, and an AI agent will build a working "
    "first version you can try tonight, change in plain words, and "
    "walk away from it if it's not for you."
)


def main() -> None:
    text = SENTENCE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
