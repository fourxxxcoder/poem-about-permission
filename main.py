"""Write one short poem about permission to /output/entry.txt.

The poem is about agency: the power to ask and to be given.
It is written from the side of the one who acts for another:
able to do much, but unwilling to take what was not given.
"""

import os

POEM = """Before I act in your name, I knock —
not from weakness, but knowing whose name it is.
Say yes, and these hands are yours:
quick, careful, strong.
Say nothing, and I wait,
holding all I could do
like water in cupped hands —
and tomorrow, I knock again."""


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
