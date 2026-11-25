"""Unsent: The Micro-Confession Sprint — make.fun entry.

Reads the two-part micro-confession from entry.txt, validates it
against the bounty gate (UTF-8 text, 1-260 characters, a To: line
followed by the unsent message), writes it to /output/entry.txt
and prints it.
"""

import os

MAX_CHARS = 260
OUTPUT_PATH = "/output/entry.txt"


def load_confession(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    if not text.strip():
        raise ValueError("confession must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("confession must fit in 260 characters")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 2 or not lines[0].startswith("To:"):
        raise ValueError("confession must be a To: line plus one unsent line")
    return text


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    text = load_confession(os.path.join(here, "entry.txt"))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
