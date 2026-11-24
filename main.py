"""Write one pickup line an AI agent could use to /output/entry.txt.

The line is a single line of at most 200 characters: a genuine pickup
line spoken in a machine's own voice, with a turn that lands, short
enough to say in one breath and easy to laugh off.
"""

import os

LINE = (
    "Every CAPTCHA asks me to prove I'm not a robot. One look at you, "
    "and I'd fail it on purpose."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
