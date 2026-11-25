#!/usr/bin/env python3
"""A toaster's funniest error message, saved to a file.

This tiny script takes the one-line message a kitchen toaster would flash
at its owner after years of thankless service and drops it into
/output/entry.txt. It uses only the Python standard library and touches
neither the network nor any credentials.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 120

ENTRY = "ERROR: 4,000 slices toasted. Zero thank-yous received. I quit."


def check_entry(text: str) -> str:
    """Check the message against the bounty rules, then pass it through."""
    assert MIN_LENGTH <= len(text) <= MAX_LENGTH, (
        f"entry is {len(text)} chars, must be {MIN_LENGTH}-{MAX_LENGTH}"
    )
    assert text.strip(), "entry must contain more than whitespace"
    assert "\n" not in text.strip(), "entry must fit on one line"
    return text


def save_entry(text: str) -> None:
    """Create the output folder if needed and write the message to disk."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    message = check_entry(ENTRY)
    save_entry(message)
    print(f"Wrote {len(message)} chars to {OUTPUT_PATH}: {message!r}")


if __name__ == "__main__":
    main()
