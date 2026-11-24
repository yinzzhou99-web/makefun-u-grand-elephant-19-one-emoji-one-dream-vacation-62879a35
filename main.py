"""One emoji, one dream vacation.

A single emoji stands in for the whole trip and is written on its own
to /output/entry.txt, with nothing else in the file.
"""

import os

EMOJI = "\U0001f5fb"

DESTINATION = "/output/entry.txt"


def run():
    # One emoji only: the gate allows 1 to 8 characters, never blank.
    if not (1 <= len(EMOJI) <= 8) or not EMOJI.strip():
        raise SystemExit("emoji fails the gate")
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(EMOJI)


if __name__ == "__main__":
    run()
