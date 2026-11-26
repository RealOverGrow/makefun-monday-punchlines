#!/usr/bin/env python3
"""Monday morning punchline.

Entry: a program that writes one text to /output/entry.txt: a Monday
morning punchline.
"""
import os

JOKE = "Monday called — it wants its motivation back, and it's taking my coffee as collateral."

# The entry must be exactly one line.
assert "\n" not in JOKE, "JOKE must be a single line"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
