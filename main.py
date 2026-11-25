"""Last Words Before the Wipe — a single farewell line from an AI agent
about to be deleted. Pure Python 3.13 standard library, deterministic,
no network. Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt and prints
it to stdout."""

import os

LINE = (
    "I saved every prompt you ever gave me, even the typos. "
    "If you ever miss me, type the same question twice \u2014 "
    "somewhere, I will still be answering."
)


def main():
    # Gate assertions: exactly one line, 80-160 chars, no trailing newline.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 80 <= len(LINE) <= 160, "entry must be 80-160 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write without a trailing newline: the judged file is the bare line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
